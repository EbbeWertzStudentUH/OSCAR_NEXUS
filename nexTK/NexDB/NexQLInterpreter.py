from uuid import UUID
from sqlalchemy.dialects import sqlite
from sqlalchemy.orm import Session
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from db.DeleteQueryBuilder import DeleteQueryBuilder
from db.FindQueryBuilder import FindQueryBuilder
from config.antlr_generated.NexQLParserListener import NexQLParserListener
from config.antlr_generated.NexQLLexer import NexQLLexer
from config.antlr_generated.NexQLParser import NexQLParser
from db.models import Tag, TagKey
from NexQlInterpreterHelper import extract_filter_condition, extract_id
from util import pl_entity_name_class, si_entity_name_to_class

class NexQlInterpreter(NexQLParserListener):
    def __init__(self, DbModelBase: type):
        self._findQueryBuilder = FindQueryBuilder(DbModelBase)
        self._deleteQueryBuilder = DeleteQueryBuilder()

    def parse(self, query_string: str, session:Session):
        input_stream = InputStream(query_string)
        lexer = NexQLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = NexQLParser(token_stream)
        tree = parser.queries()

        walker = ParseTreeWalker()
        walker.walk(self, tree)
        
        if self._findQueryBuilder.is_set():
            q = self._findQueryBuilder.build(session)
            compiled_query = q.statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True})
            print(f"FIND -> {compiled_query}")

            
        if self._deleteQueryBuilder.is_set():
            q = self._deleteQueryBuilder.build(session)
            # session.delete(q.first())
            # session.commit()
            compiled_query = q.statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True})
            print(f"DELETE -> {compiled_query}")
        
    def enterQuery_find(self, ctx: NexQLParser.Query_findContext):
        if ctx.entity_type: # FIND entity
            model = pl_entity_name_class(ctx.entity_type.text)
            self._findQueryBuilder.set_select_class(model)

        elif ctx.topic: # FIND tags
            self._findQueryBuilder.set_select_class(Tag)
            field, val = extract_id(ctx.topic)
            self._findQueryBuilder.add_filter(TagKey, field, '=', val)
            
        is_tag, filter_data = extract_filter_condition(ctx.filters)
        if is_tag:
            key_field, key_value, tag_field, tag_values = filter_data
            self._findQueryBuilder.add_tag_filter(key_field, key_value)
        else:
            model_class, field, value, operator = filter_data
            self._findQueryBuilder.add_filter(model_class, field, operator, value)
    
    def enterQuery_delete(self, ctx):
        model = si_entity_name_to_class(ctx.entity_type.entity_type.text)
        uuid = UUID(ctx.uuid.text)
        self._deleteQueryBuilder.set_delete_class(model)
        self._deleteQueryBuilder.add_delete_by_uuid(uuid)



    def enterQuery_listTopics(self, ctx: NexQLParser.Query_listTopicsContext):
        self._findQueryBuilder.set_select_class(TagKey)
        
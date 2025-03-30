import operator
from uuid import UUID
from sqlalchemy.dialects import sqlite

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from db.QueryBuilder import QueryBuilder
from config.antlr_generated.NexQLParserListener import NexQLParserListener
from config.antlr_generated.NexQLLexer import NexQLLexer
from config.antlr_generated.NexQLParser import NexQLParser
from db.models import Tag, TagKey
from util import plural_entity_name_to_model_class

class NexQlInterpreter(NexQLParserListener):
    def __init__(self, DbModelBase: type):
        self._queryBuilder = QueryBuilder(DbModelBase)

    def parse(self, query_string: str, session):
        input_stream = InputStream(query_string)
        lexer = NexQLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = NexQLParser(token_stream)
        tree = parser.queries()

        walker = ParseTreeWalker()
        walker.walk(self, tree)
        q = self._queryBuilder.build(session)
        compiled_query = q.statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True})
        print(str(compiled_query))

    def enterQuery_find(self, ctx: NexQLParser.Query_findContext):
        if ctx.entity_type: # FIND entity
            model = plural_entity_name_to_model_class(ctx.entity_type.text)
            self._queryBuilder.set_select_class(model)

        elif ctx.topic: # FIND tags
            self._queryBuilder.set_select_class(Tag)
            field, val = self.extract_id_simple(ctx.topic)
            self._queryBuilder.add_filter(TagKey, field, '=', val)
    

    def extract_id_simple(self, ctx:NexQLParser.Id_simpleContext) -> tuple[str, object]:
        if isinstance(ctx, NexQLParser.Id_uuidContext):
            return "id", UUID(ctx.identifier.text)
        elif isinstance(ctx, NexQLParser.Id_nameContext):
            return "name", ctx.identifier.text

    def enterQuery_listTopics(self, ctx: NexQLParser.Query_listTopicsContext):
        self._queryBuilder.set_select_class(TagKey)

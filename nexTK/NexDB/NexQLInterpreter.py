from pydantic_core import to_json
from sqlalchemy.orm import Session
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from queriers.FindQuerier import FindQuerier
from config.antlr_generated.NexQLParserListener import NexQLParserListener
from config.antlr_generated.NexQLLexer import NexQLLexer
from config.antlr_generated.NexQLParser import NexQLParser
from query_models.reading_query_models import FindQuery, SearchQuery


def to_json_(obj, filename='debug_output.json'):
    json_str = to_json(obj, indent=2).decode()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json_str)


class NexQlInterpreter(NexQLParserListener):
    def __init__(self, DbModelBase: type):
        self._find_querier = FindQuerier(DbModelBase)
        # self._findQueryBuilder = FindQueryBuilder(DbModelBase)
        # self._deleteQueryBuilder = DeleteQueryBuilder()
        # TODO RESET

    def parse(self, query_string: str, session:Session):
        self._find_querier.set_session(self._session)
        input_stream = InputStream(query_string)
        lexer = NexQLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = NexQLParser(token_stream)
        tree = parser.queries()

        walker = ParseTreeWalker()
        walker.walk(self, tree)
        
        # if self._findQueryBuilder.is_set():
        #     q = self._findQueryBuilder.build(session)
        #     compiled_query = q.statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True})
        #     print(f"\n\nFIND ->\n {compiled_query}")
        #
        #
        # if self._deleteQueryBuilder.is_set():
        #     q = self._deleteQueryBuilder.build(session)
        #     # session.delete(q.first())
        #     # session.commit()
        #     compiled_query = q.statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True})
        #     print(f"\n\nDELETE ->\n {compiled_query}")
        
    def enterQuery_find(self, ctx: NexQLParser.Query_findContext):
        query_model = FindQuery.from_context(ctx)
        to_json_(query_model)
        result = self._find_querier.query_find(query_model)
        print(f"result: {result}")


    def enterQuery_search(self, ctx:NexQLParser.Query_searchContext):
        query_model = SearchQuery.from_context(ctx)
        to_json_(query_model)
    
    # def enterQuery_delete(self, ctx):
    #     model = si_entity_name_to_class(ctx.entity_type.entity_type.text)
    #     uuid = UUID(ctx.uuid.text)
    #     self._deleteQueryBuilder.set_delete_class(model)
    #     self._deleteQueryBuilder.add_delete_by_uuid(uuid)



    # def enterQuery_listTopics(self, ctx: NexQLParser.Query_listTopicsContext):
    #     self._findQueryBuilder.set_select_class(TagKey)
        
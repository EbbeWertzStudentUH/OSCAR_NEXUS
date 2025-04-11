from antlr4.error.ErrorListener import ErrorListener
from sqlalchemy.orm import Session
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from Exceptions import NexQlSyntaxException
from queriers.CollectQuerier import CollectQuerier
from queriers.CreateQuerier import CreateQuerier
from queriers.FindQuerier import FindQuerier
from config.antlr_generated.NexQLParserListener import NexQLParserListener
from config.antlr_generated.NexQLLexer import NexQLLexer
from config.antlr_generated.NexQLParser import NexQLParser
from queriers.SearchQuerier import SearchQuerier
from queriers.TaggerQuerier import TaggerQuerier
from query_models.mutating_query_models import TagAssignQuery, TagTopicCreateQuery, TagCreateQuery, \
    CollectionCreateQuery, SchemaCreateQuery
from query_models.reading_query_models import FindQuery, SearchQuery, CollectQuery



class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise NexQlSyntaxException(f"Syntax error at line {line}:{column} - {msg}")

class NexQLEngine(NexQLParserListener):
    def __init__(self, DbModelBase: type):
        self._find_querier = FindQuerier(DbModelBase)
        self._search_querier = SearchQuerier()
        self._collect_querier = CollectQuerier()
        self._create_querier = CreateQuerier()
        self._tagger_querier = TaggerQuerier()

        self._query_result = None

    def get_query_result(self):
        return {obj.id: obj.name for obj in self._query_result}

    def parse(self, query_string: str, session:Session):
        self._find_querier.set_session(session)
        self._search_querier.set_session(session)
        self._collect_querier.set_session(session)
        self._create_querier.set_session(session)
        self._tagger_querier.set_session(session)

        input_stream = InputStream(query_string)
        lexer = NexQLLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ThrowingErrorListener())
        token_stream = CommonTokenStream(lexer)
        parser = NexQLParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener())
        tree = parser.queries()

        walker = ParseTreeWalker()
        walker.walk(self, tree)
        
    def enterQuery_find(self, ctx: NexQLParser.Query_findContext):
        query_model = FindQuery.from_context(ctx)
        result = self._find_querier.query_find(query_model)
        self._query_result = result

    def enterQuery_search(self, ctx:NexQLParser.Query_searchContext):
        query_model = SearchQuery.from_context(ctx)
        result = self._search_querier.query_search(query_model)
        self._query_result = result

    def enterQuery_collect(self, ctx:NexQLParser.Query_collectContext):
        query_model = CollectQuery.from_context(ctx)
        self._collect_querier.query_colect(query_model)
        self._query_result = None

    def enterQuery_tag(self, ctx:NexQLParser.Query_tagContext):
        query_model = TagAssignQuery.from_context(ctx)
        self._tagger_querier.query_tag(query_model)
        self._query_result = None

    def enterCreate_tag_key(self, ctx:NexQLParser.Create_tag_keyContext):
        query_model = TagTopicCreateQuery.from_context(ctx)
        self._create_querier.query_create_topic(query_model)
        self._query_result = None

    def enterCreate_tag_value(self, ctx:NexQLParser.Create_tag_valueContext):
        query_model = TagCreateQuery.from_context(ctx)
        self._create_querier.query_create_tag(query_model)
        self._query_result = None

    def enterCreate_collection(self, ctx:NexQLParser.Create_collectionContext):
        query_model = CollectionCreateQuery.from_context(ctx)
        self._create_querier.query_create_collection(query_model)
        self._query_result = None

    def enterCreate_schema(self, ctx:NexQLParser.Create_schemaContext):
        query_model = SchemaCreateQuery.from_context(ctx)
        self._create_querier.query_create_schema(query_model)
        self._query_result = None

        
// Generated from c:/Users/ebbew/Desktop/OSCAR_NEXUS/QueryLanguage.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class QueryLanguageParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, ENTITY_TYPE=23, ENTITY_TYPE_PLURAL=24, 
		FILTERABLE_PROPERTY=25, SHOWABLE_PROPERTY=26, COLLECTION_IDENTIFIER=27, 
		SCHEMA_IDENTIFIER=28, TAG_IDENTIFIER=29, CONSTANT_IDENTIFIER=30, BATCH_IDENTIFIER=31, 
		DATASET_IDENTIFIER=32, IDENTIFIER=33, LITERAL_VALUE=34, WILDCARD_STRING_LITERAL=35, 
		STRING_LITERAL=36, DATATYPE=37, COMPARISON_OPERATOR=38, UNION_OPERATOR=39, 
		UUID=40, NUMBER=41, WS=42;
	public static final int
		RULE_query = 0, RULE_findstatement = 1, RULE_collectstatement = 2, RULE_loadstatement = 3, 
		RULE_deletestatement = 4, RULE_createstatement = 5, RULE_create_tag_key_statement = 6, 
		RULE_create_tag_value_statement = 7, RULE_create_schema_statement = 8, 
		RULE_create_collection_statement = 9, RULE_schema_body = 10, RULE_fields_defenition = 11, 
		RULE_field_defenition = 12, RULE_discovery_clause = 13, RULE_discovery_clause_with_match = 14, 
		RULE_collection_include_clause = 15, RULE_filter_clause = 16, RULE_filter_condition = 17, 
		RULE_property_name_filter_condition = 18, RULE_property_value_filter_condition = 19, 
		RULE_tag_filter_condition = 20, RULE_match_clause = 21, RULE_collection_expression = 22, 
		RULE_result_specifiers = 23, RULE_columns_specifier = 24, RULE_constants_specifier = 25, 
		RULE_show_specifier = 26, RULE_limit_specifier = 27;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "findstatement", "collectstatement", "loadstatement", "deletestatement", 
			"createstatement", "create_tag_key_statement", "create_tag_value_statement", 
			"create_schema_statement", "create_collection_statement", "schema_body", 
			"fields_defenition", "field_defenition", "discovery_clause", "discovery_clause_with_match", 
			"collection_include_clause", "filter_clause", "filter_condition", "property_name_filter_condition", 
			"property_value_filter_condition", "tag_filter_condition", "match_clause", 
			"collection_expression", "result_specifiers", "columns_specifier", "constants_specifier", 
			"show_specifier", "limit_specifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'FIND'", "'COLLECT'", "'DEEP'", "'AS'", "'LOAD'", "'DELETE'", 
			"'CREATE'", "'TAG'", "'FOR'", "'SCHEMA'", "'COLLECTION'", "'FROM'", "'INFO'", 
			"'COLUMNS'", "'CONSTANTS'", "','", "'IN'", "'FILTER'", "'='", "'MATCH'", 
			"'SHOW'", "'LIMIT'", null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "'STRING'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "ENTITY_TYPE", 
			"ENTITY_TYPE_PLURAL", "FILTERABLE_PROPERTY", "SHOWABLE_PROPERTY", "COLLECTION_IDENTIFIER", 
			"SCHEMA_IDENTIFIER", "TAG_IDENTIFIER", "CONSTANT_IDENTIFIER", "BATCH_IDENTIFIER", 
			"DATASET_IDENTIFIER", "IDENTIFIER", "LITERAL_VALUE", "WILDCARD_STRING_LITERAL", 
			"STRING_LITERAL", "DATATYPE", "COMPARISON_OPERATOR", "UNION_OPERATOR", 
			"UUID", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "QueryLanguage.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public QueryLanguageParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public FindstatementContext findstatement() {
			return getRuleContext(FindstatementContext.class,0);
		}
		public CollectstatementContext collectstatement() {
			return getRuleContext(CollectstatementContext.class,0);
		}
		public LoadstatementContext loadstatement() {
			return getRuleContext(LoadstatementContext.class,0);
		}
		public CreatestatementContext createstatement() {
			return getRuleContext(CreatestatementContext.class,0);
		}
		public DeletestatementContext deletestatement() {
			return getRuleContext(DeletestatementContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_query);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				findstatement();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				collectstatement();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 3);
				{
				setState(58);
				loadstatement();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 4);
				{
				setState(59);
				createstatement();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				deletestatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindstatementContext extends ParserRuleContext {
		public TerminalNode ENTITY_TYPE_PLURAL() { return getToken(QueryLanguageParser.ENTITY_TYPE_PLURAL, 0); }
		public Discovery_clauseContext discovery_clause() {
			return getRuleContext(Discovery_clauseContext.class,0);
		}
		public Result_specifiersContext result_specifiers() {
			return getRuleContext(Result_specifiersContext.class,0);
		}
		public FindstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findstatement; }
	}

	public final FindstatementContext findstatement() throws RecognitionException {
		FindstatementContext _localctx = new FindstatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_findstatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(T__0);
			setState(64);
			match(ENTITY_TYPE_PLURAL);
			setState(65);
			discovery_clause();
			setState(66);
			result_specifiers();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CollectstatementContext extends ParserRuleContext {
		public TerminalNode SCHEMA_IDENTIFIER() { return getToken(QueryLanguageParser.SCHEMA_IDENTIFIER, 0); }
		public Discovery_clause_with_matchContext discovery_clause_with_match() {
			return getRuleContext(Discovery_clause_with_matchContext.class,0);
		}
		public TerminalNode COLLECTION_IDENTIFIER() { return getToken(QueryLanguageParser.COLLECTION_IDENTIFIER, 0); }
		public CollectstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_collectstatement; }
	}

	public final CollectstatementContext collectstatement() throws RecognitionException {
		CollectstatementContext _localctx = new CollectstatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_collectstatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(T__1);
			setState(70);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(69);
				match(T__2);
				}
			}

			setState(72);
			match(SCHEMA_IDENTIFIER);
			setState(73);
			discovery_clause_with_match();
			setState(74);
			match(T__3);
			setState(75);
			match(COLLECTION_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoadstatementContext extends ParserRuleContext {
		public TerminalNode DATASET_IDENTIFIER() { return getToken(QueryLanguageParser.DATASET_IDENTIFIER, 0); }
		public Result_specifiersContext result_specifiers() {
			return getRuleContext(Result_specifiersContext.class,0);
		}
		public LoadstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loadstatement; }
	}

	public final LoadstatementContext loadstatement() throws RecognitionException {
		LoadstatementContext _localctx = new LoadstatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_loadstatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(T__4);
			setState(78);
			match(DATASET_IDENTIFIER);
			setState(79);
			result_specifiers();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeletestatementContext extends ParserRuleContext {
		public TerminalNode UUID() { return getToken(QueryLanguageParser.UUID, 0); }
		public DeletestatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deletestatement; }
	}

	public final DeletestatementContext deletestatement() throws RecognitionException {
		DeletestatementContext _localctx = new DeletestatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_deletestatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__5);
			setState(82);
			match(UUID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreatestatementContext extends ParserRuleContext {
		public Create_tag_key_statementContext create_tag_key_statement() {
			return getRuleContext(Create_tag_key_statementContext.class,0);
		}
		public Create_tag_value_statementContext create_tag_value_statement() {
			return getRuleContext(Create_tag_value_statementContext.class,0);
		}
		public Create_schema_statementContext create_schema_statement() {
			return getRuleContext(Create_schema_statementContext.class,0);
		}
		public Create_collection_statementContext create_collection_statement() {
			return getRuleContext(Create_collection_statementContext.class,0);
		}
		public CreatestatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createstatement; }
	}

	public final CreatestatementContext createstatement() throws RecognitionException {
		CreatestatementContext _localctx = new CreatestatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_createstatement);
		try {
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				create_tag_key_statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				create_tag_value_statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(86);
				create_schema_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(87);
				create_collection_statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Create_tag_key_statementContext extends ParserRuleContext {
		public TerminalNode TAG_IDENTIFIER() { return getToken(QueryLanguageParser.TAG_IDENTIFIER, 0); }
		public Create_tag_key_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create_tag_key_statement; }
	}

	public final Create_tag_key_statementContext create_tag_key_statement() throws RecognitionException {
		Create_tag_key_statementContext _localctx = new Create_tag_key_statementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_create_tag_key_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(T__6);
			setState(91);
			match(T__7);
			setState(92);
			match(TAG_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Create_tag_value_statementContext extends ParserRuleContext {
		public List<TerminalNode> TAG_IDENTIFIER() { return getTokens(QueryLanguageParser.TAG_IDENTIFIER); }
		public TerminalNode TAG_IDENTIFIER(int i) {
			return getToken(QueryLanguageParser.TAG_IDENTIFIER, i);
		}
		public Create_tag_value_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create_tag_value_statement; }
	}

	public final Create_tag_value_statementContext create_tag_value_statement() throws RecognitionException {
		Create_tag_value_statementContext _localctx = new Create_tag_value_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_create_tag_value_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__6);
			setState(95);
			match(T__7);
			setState(96);
			match(TAG_IDENTIFIER);
			setState(97);
			match(T__8);
			setState(98);
			match(TAG_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Create_schema_statementContext extends ParserRuleContext {
		public TerminalNode SCHEMA_IDENTIFIER() { return getToken(QueryLanguageParser.SCHEMA_IDENTIFIER, 0); }
		public Schema_bodyContext schema_body() {
			return getRuleContext(Schema_bodyContext.class,0);
		}
		public Create_schema_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create_schema_statement; }
	}

	public final Create_schema_statementContext create_schema_statement() throws RecognitionException {
		Create_schema_statementContext _localctx = new Create_schema_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_create_schema_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(T__6);
			setState(101);
			match(T__9);
			setState(102);
			match(SCHEMA_IDENTIFIER);
			setState(103);
			schema_body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Create_collection_statementContext extends ParserRuleContext {
		public TerminalNode COLLECTION_IDENTIFIER() { return getToken(QueryLanguageParser.COLLECTION_IDENTIFIER, 0); }
		public Create_collection_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create_collection_statement; }
	}

	public final Create_collection_statementContext create_collection_statement() throws RecognitionException {
		Create_collection_statementContext _localctx = new Create_collection_statementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_create_collection_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(T__6);
			setState(106);
			match(T__10);
			setState(107);
			match(T__11);
			setState(108);
			match(COLLECTION_IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Schema_bodyContext extends ParserRuleContext {
		public List<Fields_defenitionContext> fields_defenition() {
			return getRuleContexts(Fields_defenitionContext.class);
		}
		public Fields_defenitionContext fields_defenition(int i) {
			return getRuleContext(Fields_defenitionContext.class,i);
		}
		public TerminalNode STRING_LITERAL() { return getToken(QueryLanguageParser.STRING_LITERAL, 0); }
		public Schema_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_schema_body; }
	}

	public final Schema_bodyContext schema_body() throws RecognitionException {
		Schema_bodyContext _localctx = new Schema_bodyContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_schema_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(110);
				match(T__12);
				setState(111);
				match(STRING_LITERAL);
				}
			}

			setState(114);
			match(T__13);
			setState(115);
			fields_defenition();
			setState(116);
			match(T__14);
			setState(117);
			fields_defenition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Fields_defenitionContext extends ParserRuleContext {
		public List<Field_defenitionContext> field_defenition() {
			return getRuleContexts(Field_defenitionContext.class);
		}
		public Field_defenitionContext field_defenition(int i) {
			return getRuleContext(Field_defenitionContext.class,i);
		}
		public Fields_defenitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fields_defenition; }
	}

	public final Fields_defenitionContext fields_defenition() throws RecognitionException {
		Fields_defenitionContext _localctx = new Fields_defenitionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_fields_defenition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			field_defenition();
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(120);
				match(T__15);
				setState(121);
				field_defenition();
				}
				}
				setState(126);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Field_defenitionContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(QueryLanguageParser.IDENTIFIER, 0); }
		public TerminalNode DATATYPE() { return getToken(QueryLanguageParser.DATATYPE, 0); }
		public Field_defenitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_defenition; }
	}

	public final Field_defenitionContext field_defenition() throws RecognitionException {
		Field_defenitionContext _localctx = new Field_defenitionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_field_defenition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(IDENTIFIER);
			setState(128);
			match(DATATYPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Discovery_clauseContext extends ParserRuleContext {
		public Filter_clauseContext filter_clause() {
			return getRuleContext(Filter_clauseContext.class,0);
		}
		public Collection_include_clauseContext collection_include_clause() {
			return getRuleContext(Collection_include_clauseContext.class,0);
		}
		public Discovery_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_discovery_clause; }
	}

	public final Discovery_clauseContext discovery_clause() throws RecognitionException {
		Discovery_clauseContext _localctx = new Discovery_clauseContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_discovery_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(130);
				collection_include_clause();
				}
			}

			setState(133);
			filter_clause();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Discovery_clause_with_matchContext extends ParserRuleContext {
		public Collection_include_clauseContext collection_include_clause() {
			return getRuleContext(Collection_include_clauseContext.class,0);
		}
		public List<Filter_clauseContext> filter_clause() {
			return getRuleContexts(Filter_clauseContext.class);
		}
		public Filter_clauseContext filter_clause(int i) {
			return getRuleContext(Filter_clauseContext.class,i);
		}
		public List<Match_clauseContext> match_clause() {
			return getRuleContexts(Match_clauseContext.class);
		}
		public Match_clauseContext match_clause(int i) {
			return getRuleContext(Match_clauseContext.class,i);
		}
		public Discovery_clause_with_matchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_discovery_clause_with_match; }
	}

	public final Discovery_clause_with_matchContext discovery_clause_with_match() throws RecognitionException {
		Discovery_clause_with_matchContext _localctx = new Discovery_clause_with_matchContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_discovery_clause_with_match);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(135);
				collection_include_clause();
				}
			}

			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17 || _la==T__19) {
				{
				setState(140);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__17:
					{
					setState(138);
					filter_clause();
					}
					break;
				case T__19:
					{
					setState(139);
					match_clause();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Collection_include_clauseContext extends ParserRuleContext {
		public Collection_expressionContext collection_expression() {
			return getRuleContext(Collection_expressionContext.class,0);
		}
		public Collection_include_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_collection_include_clause; }
	}

	public final Collection_include_clauseContext collection_include_clause() throws RecognitionException {
		Collection_include_clauseContext _localctx = new Collection_include_clauseContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_collection_include_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(T__16);
			setState(146);
			collection_expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Filter_clauseContext extends ParserRuleContext {
		public Filter_conditionContext filter_condition() {
			return getRuleContext(Filter_conditionContext.class,0);
		}
		public Filter_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filter_clause; }
	}

	public final Filter_clauseContext filter_clause() throws RecognitionException {
		Filter_clauseContext _localctx = new Filter_clauseContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_filter_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__17);
			setState(149);
			filter_condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Filter_conditionContext extends ParserRuleContext {
		public Property_name_filter_conditionContext property_name_filter_condition() {
			return getRuleContext(Property_name_filter_conditionContext.class,0);
		}
		public Property_value_filter_conditionContext property_value_filter_condition() {
			return getRuleContext(Property_value_filter_conditionContext.class,0);
		}
		public Tag_filter_conditionContext tag_filter_condition() {
			return getRuleContext(Tag_filter_conditionContext.class,0);
		}
		public Filter_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filter_condition; }
	}

	public final Filter_conditionContext filter_condition() throws RecognitionException {
		Filter_conditionContext _localctx = new Filter_conditionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_filter_condition);
		try {
			setState(154);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENTITY_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				property_name_filter_condition();
				}
				break;
			case FILTERABLE_PROPERTY:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				property_value_filter_condition();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 3);
				{
				setState(153);
				tag_filter_condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Property_name_filter_conditionContext extends ParserRuleContext {
		public TerminalNode ENTITY_TYPE() { return getToken(QueryLanguageParser.ENTITY_TYPE, 0); }
		public TerminalNode WILDCARD_STRING_LITERAL() { return getToken(QueryLanguageParser.WILDCARD_STRING_LITERAL, 0); }
		public Property_name_filter_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_property_name_filter_condition; }
	}

	public final Property_name_filter_conditionContext property_name_filter_condition() throws RecognitionException {
		Property_name_filter_conditionContext _localctx = new Property_name_filter_conditionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_property_name_filter_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(ENTITY_TYPE);
			setState(157);
			match(T__18);
			setState(158);
			match(WILDCARD_STRING_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Property_value_filter_conditionContext extends ParserRuleContext {
		public TerminalNode FILTERABLE_PROPERTY() { return getToken(QueryLanguageParser.FILTERABLE_PROPERTY, 0); }
		public TerminalNode COMPARISON_OPERATOR() { return getToken(QueryLanguageParser.COMPARISON_OPERATOR, 0); }
		public TerminalNode LITERAL_VALUE() { return getToken(QueryLanguageParser.LITERAL_VALUE, 0); }
		public Property_value_filter_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_property_value_filter_condition; }
	}

	public final Property_value_filter_conditionContext property_value_filter_condition() throws RecognitionException {
		Property_value_filter_conditionContext _localctx = new Property_value_filter_conditionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_property_value_filter_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(FILTERABLE_PROPERTY);
			setState(161);
			match(COMPARISON_OPERATOR);
			setState(162);
			match(LITERAL_VALUE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tag_filter_conditionContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(QueryLanguageParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(QueryLanguageParser.IDENTIFIER, i);
		}
		public Tag_filter_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tag_filter_condition; }
	}

	public final Tag_filter_conditionContext tag_filter_condition() throws RecognitionException {
		Tag_filter_conditionContext _localctx = new Tag_filter_conditionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_tag_filter_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(IDENTIFIER);
			setState(165);
			match(T__18);
			setState(166);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Match_clauseContext extends ParserRuleContext {
		public TerminalNode CONSTANT_IDENTIFIER() { return getToken(QueryLanguageParser.CONSTANT_IDENTIFIER, 0); }
		public TerminalNode COMPARISON_OPERATOR() { return getToken(QueryLanguageParser.COMPARISON_OPERATOR, 0); }
		public TerminalNode LITERAL_VALUE() { return getToken(QueryLanguageParser.LITERAL_VALUE, 0); }
		public Match_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_match_clause; }
	}

	public final Match_clauseContext match_clause() throws RecognitionException {
		Match_clauseContext _localctx = new Match_clauseContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_match_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__19);
			setState(169);
			match(CONSTANT_IDENTIFIER);
			setState(170);
			match(COMPARISON_OPERATOR);
			setState(171);
			match(LITERAL_VALUE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Collection_expressionContext extends ParserRuleContext {
		public List<TerminalNode> COLLECTION_IDENTIFIER() { return getTokens(QueryLanguageParser.COLLECTION_IDENTIFIER); }
		public TerminalNode COLLECTION_IDENTIFIER(int i) {
			return getToken(QueryLanguageParser.COLLECTION_IDENTIFIER, i);
		}
		public List<TerminalNode> UNION_OPERATOR() { return getTokens(QueryLanguageParser.UNION_OPERATOR); }
		public TerminalNode UNION_OPERATOR(int i) {
			return getToken(QueryLanguageParser.UNION_OPERATOR, i);
		}
		public Collection_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_collection_expression; }
	}

	public final Collection_expressionContext collection_expression() throws RecognitionException {
		Collection_expressionContext _localctx = new Collection_expressionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_collection_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(COLLECTION_IDENTIFIER);
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==UNION_OPERATOR) {
				{
				{
				setState(174);
				match(UNION_OPERATOR);
				setState(175);
				match(COLLECTION_IDENTIFIER);
				}
				}
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Result_specifiersContext extends ParserRuleContext {
		public Columns_specifierContext columns_specifier() {
			return getRuleContext(Columns_specifierContext.class,0);
		}
		public Constants_specifierContext constants_specifier() {
			return getRuleContext(Constants_specifierContext.class,0);
		}
		public Show_specifierContext show_specifier() {
			return getRuleContext(Show_specifierContext.class,0);
		}
		public Limit_specifierContext limit_specifier() {
			return getRuleContext(Limit_specifierContext.class,0);
		}
		public Result_specifiersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_result_specifiers; }
	}

	public final Result_specifiersContext result_specifiers() throws RecognitionException {
		Result_specifiersContext _localctx = new Result_specifiersContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_result_specifiers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(181);
				columns_specifier();
				}
			}

			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(184);
				constants_specifier();
				}
			}

			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(187);
				show_specifier();
				}
			}

			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__21) {
				{
				setState(190);
				limit_specifier();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Columns_specifierContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(QueryLanguageParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(QueryLanguageParser.IDENTIFIER, i);
		}
		public Columns_specifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_columns_specifier; }
	}

	public final Columns_specifierContext columns_specifier() throws RecognitionException {
		Columns_specifierContext _localctx = new Columns_specifierContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_columns_specifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(T__13);
			setState(194);
			match(IDENTIFIER);
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(195);
				match(T__15);
				setState(196);
				match(IDENTIFIER);
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Constants_specifierContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(QueryLanguageParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(QueryLanguageParser.IDENTIFIER, i);
		}
		public Constants_specifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constants_specifier; }
	}

	public final Constants_specifierContext constants_specifier() throws RecognitionException {
		Constants_specifierContext _localctx = new Constants_specifierContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_constants_specifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(T__14);
			setState(203);
			match(IDENTIFIER);
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(204);
				match(T__15);
				setState(205);
				match(IDENTIFIER);
				}
				}
				setState(210);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Show_specifierContext extends ParserRuleContext {
		public List<TerminalNode> SHOWABLE_PROPERTY() { return getTokens(QueryLanguageParser.SHOWABLE_PROPERTY); }
		public TerminalNode SHOWABLE_PROPERTY(int i) {
			return getToken(QueryLanguageParser.SHOWABLE_PROPERTY, i);
		}
		public Show_specifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_show_specifier; }
	}

	public final Show_specifierContext show_specifier() throws RecognitionException {
		Show_specifierContext _localctx = new Show_specifierContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_show_specifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(T__20);
			setState(212);
			match(SHOWABLE_PROPERTY);
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(213);
				match(T__15);
				setState(214);
				match(SHOWABLE_PROPERTY);
				}
				}
				setState(219);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Limit_specifierContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(QueryLanguageParser.NUMBER, 0); }
		public Limit_specifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_limit_specifier; }
	}

	public final Limit_specifierContext limit_specifier() throws RecognitionException {
		Limit_specifierContext _localctx = new Limit_specifierContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_limit_specifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(T__21);
			setState(221);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001*\u00e0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000"+
		">\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0003\u0002G\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005Y\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0003\nq\b\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0005\u000b{\b\u000b\n\u000b\f\u000b~\t\u000b\u0001\f\u0001\f\u0001\f"+
		"\u0001\r\u0003\r\u0084\b\r\u0001\r\u0001\r\u0001\u000e\u0003\u000e\u0089"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u008d\b\u000e\n\u000e\f\u000e"+
		"\u0090\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u009b\b\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0005\u0016\u00b1\b\u0016\n\u0016\f\u0016\u00b4"+
		"\t\u0016\u0001\u0017\u0003\u0017\u00b7\b\u0017\u0001\u0017\u0003\u0017"+
		"\u00ba\b\u0017\u0001\u0017\u0003\u0017\u00bd\b\u0017\u0001\u0017\u0003"+
		"\u0017\u00c0\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0005"+
		"\u0018\u00c6\b\u0018\n\u0018\f\u0018\u00c9\t\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0005\u0019\u00cf\b\u0019\n\u0019\f\u0019\u00d2"+
		"\t\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u00d8"+
		"\b\u001a\n\u001a\f\u001a\u00db\t\u001a\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0000\u0000\u001c\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.0246\u0000\u0000\u00db"+
		"\u0000=\u0001\u0000\u0000\u0000\u0002?\u0001\u0000\u0000\u0000\u0004D"+
		"\u0001\u0000\u0000\u0000\u0006M\u0001\u0000\u0000\u0000\bQ\u0001\u0000"+
		"\u0000\u0000\nX\u0001\u0000\u0000\u0000\fZ\u0001\u0000\u0000\u0000\u000e"+
		"^\u0001\u0000\u0000\u0000\u0010d\u0001\u0000\u0000\u0000\u0012i\u0001"+
		"\u0000\u0000\u0000\u0014p\u0001\u0000\u0000\u0000\u0016w\u0001\u0000\u0000"+
		"\u0000\u0018\u007f\u0001\u0000\u0000\u0000\u001a\u0083\u0001\u0000\u0000"+
		"\u0000\u001c\u0088\u0001\u0000\u0000\u0000\u001e\u0091\u0001\u0000\u0000"+
		"\u0000 \u0094\u0001\u0000\u0000\u0000\"\u009a\u0001\u0000\u0000\u0000"+
		"$\u009c\u0001\u0000\u0000\u0000&\u00a0\u0001\u0000\u0000\u0000(\u00a4"+
		"\u0001\u0000\u0000\u0000*\u00a8\u0001\u0000\u0000\u0000,\u00ad\u0001\u0000"+
		"\u0000\u0000.\u00b6\u0001\u0000\u0000\u00000\u00c1\u0001\u0000\u0000\u0000"+
		"2\u00ca\u0001\u0000\u0000\u00004\u00d3\u0001\u0000\u0000\u00006\u00dc"+
		"\u0001\u0000\u0000\u00008>\u0003\u0002\u0001\u00009>\u0003\u0004\u0002"+
		"\u0000:>\u0003\u0006\u0003\u0000;>\u0003\n\u0005\u0000<>\u0003\b\u0004"+
		"\u0000=8\u0001\u0000\u0000\u0000=9\u0001\u0000\u0000\u0000=:\u0001\u0000"+
		"\u0000\u0000=;\u0001\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000>\u0001"+
		"\u0001\u0000\u0000\u0000?@\u0005\u0001\u0000\u0000@A\u0005\u0018\u0000"+
		"\u0000AB\u0003\u001a\r\u0000BC\u0003.\u0017\u0000C\u0003\u0001\u0000\u0000"+
		"\u0000DF\u0005\u0002\u0000\u0000EG\u0005\u0003\u0000\u0000FE\u0001\u0000"+
		"\u0000\u0000FG\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0005"+
		"\u001c\u0000\u0000IJ\u0003\u001c\u000e\u0000JK\u0005\u0004\u0000\u0000"+
		"KL\u0005\u001b\u0000\u0000L\u0005\u0001\u0000\u0000\u0000MN\u0005\u0005"+
		"\u0000\u0000NO\u0005 \u0000\u0000OP\u0003.\u0017\u0000P\u0007\u0001\u0000"+
		"\u0000\u0000QR\u0005\u0006\u0000\u0000RS\u0005(\u0000\u0000S\t\u0001\u0000"+
		"\u0000\u0000TY\u0003\f\u0006\u0000UY\u0003\u000e\u0007\u0000VY\u0003\u0010"+
		"\b\u0000WY\u0003\u0012\t\u0000XT\u0001\u0000\u0000\u0000XU\u0001\u0000"+
		"\u0000\u0000XV\u0001\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000Y\u000b"+
		"\u0001\u0000\u0000\u0000Z[\u0005\u0007\u0000\u0000[\\\u0005\b\u0000\u0000"+
		"\\]\u0005\u001d\u0000\u0000]\r\u0001\u0000\u0000\u0000^_\u0005\u0007\u0000"+
		"\u0000_`\u0005\b\u0000\u0000`a\u0005\u001d\u0000\u0000ab\u0005\t\u0000"+
		"\u0000bc\u0005\u001d\u0000\u0000c\u000f\u0001\u0000\u0000\u0000de\u0005"+
		"\u0007\u0000\u0000ef\u0005\n\u0000\u0000fg\u0005\u001c\u0000\u0000gh\u0003"+
		"\u0014\n\u0000h\u0011\u0001\u0000\u0000\u0000ij\u0005\u0007\u0000\u0000"+
		"jk\u0005\u000b\u0000\u0000kl\u0005\f\u0000\u0000lm\u0005\u001b\u0000\u0000"+
		"m\u0013\u0001\u0000\u0000\u0000no\u0005\r\u0000\u0000oq\u0005$\u0000\u0000"+
		"pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000"+
		"\u0000rs\u0005\u000e\u0000\u0000st\u0003\u0016\u000b\u0000tu\u0005\u000f"+
		"\u0000\u0000uv\u0003\u0016\u000b\u0000v\u0015\u0001\u0000\u0000\u0000"+
		"w|\u0003\u0018\f\u0000xy\u0005\u0010\u0000\u0000y{\u0003\u0018\f\u0000"+
		"zx\u0001\u0000\u0000\u0000{~\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000"+
		"\u0000|}\u0001\u0000\u0000\u0000}\u0017\u0001\u0000\u0000\u0000~|\u0001"+
		"\u0000\u0000\u0000\u007f\u0080\u0005!\u0000\u0000\u0080\u0081\u0005%\u0000"+
		"\u0000\u0081\u0019\u0001\u0000\u0000\u0000\u0082\u0084\u0003\u001e\u000f"+
		"\u0000\u0083\u0082\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0086\u0003 \u0010\u0000"+
		"\u0086\u001b\u0001\u0000\u0000\u0000\u0087\u0089\u0003\u001e\u000f\u0000"+
		"\u0088\u0087\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000"+
		"\u0089\u008e\u0001\u0000\u0000\u0000\u008a\u008d\u0003 \u0010\u0000\u008b"+
		"\u008d\u0003*\u0015\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008c\u008b"+
		"\u0001\u0000\u0000\u0000\u008d\u0090\u0001\u0000\u0000\u0000\u008e\u008c"+
		"\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u001d"+
		"\u0001\u0000\u0000\u0000\u0090\u008e\u0001\u0000\u0000\u0000\u0091\u0092"+
		"\u0005\u0011\u0000\u0000\u0092\u0093\u0003,\u0016\u0000\u0093\u001f\u0001"+
		"\u0000\u0000\u0000\u0094\u0095\u0005\u0012\u0000\u0000\u0095\u0096\u0003"+
		"\"\u0011\u0000\u0096!\u0001\u0000\u0000\u0000\u0097\u009b\u0003$\u0012"+
		"\u0000\u0098\u009b\u0003&\u0013\u0000\u0099\u009b\u0003(\u0014\u0000\u009a"+
		"\u0097\u0001\u0000\u0000\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009a"+
		"\u0099\u0001\u0000\u0000\u0000\u009b#\u0001\u0000\u0000\u0000\u009c\u009d"+
		"\u0005\u0017\u0000\u0000\u009d\u009e\u0005\u0013\u0000\u0000\u009e\u009f"+
		"\u0005#\u0000\u0000\u009f%\u0001\u0000\u0000\u0000\u00a0\u00a1\u0005\u0019"+
		"\u0000\u0000\u00a1\u00a2\u0005&\u0000\u0000\u00a2\u00a3\u0005\"\u0000"+
		"\u0000\u00a3\'\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005!\u0000\u0000"+
		"\u00a5\u00a6\u0005\u0013\u0000\u0000\u00a6\u00a7\u0005!\u0000\u0000\u00a7"+
		")\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005\u0014\u0000\u0000\u00a9\u00aa"+
		"\u0005\u001e\u0000\u0000\u00aa\u00ab\u0005&\u0000\u0000\u00ab\u00ac\u0005"+
		"\"\u0000\u0000\u00ac+\u0001\u0000\u0000\u0000\u00ad\u00b2\u0005\u001b"+
		"\u0000\u0000\u00ae\u00af\u0005\'\u0000\u0000\u00af\u00b1\u0005\u001b\u0000"+
		"\u0000\u00b0\u00ae\u0001\u0000\u0000\u0000\u00b1\u00b4\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000"+
		"\u0000\u00b3-\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b7\u00030\u0018\u0000\u00b6\u00b5\u0001\u0000\u0000\u0000\u00b6"+
		"\u00b7\u0001\u0000\u0000\u0000\u00b7\u00b9\u0001\u0000\u0000\u0000\u00b8"+
		"\u00ba\u00032\u0019\u0000\u00b9\u00b8\u0001\u0000\u0000\u0000\u00b9\u00ba"+
		"\u0001\u0000\u0000\u0000\u00ba\u00bc\u0001\u0000\u0000\u0000\u00bb\u00bd"+
		"\u00034\u001a\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001"+
		"\u0000\u0000\u0000\u00bd\u00bf\u0001\u0000\u0000\u0000\u00be\u00c0\u0003"+
		"6\u001b\u0000\u00bf\u00be\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000"+
		"\u0000\u0000\u00c0/\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005\u000e\u0000"+
		"\u0000\u00c2\u00c7\u0005!\u0000\u0000\u00c3\u00c4\u0005\u0010\u0000\u0000"+
		"\u00c4\u00c6\u0005!\u0000\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000\u0000\u00c7"+
		"\u00c8\u0001\u0000\u0000\u0000\u00c81\u0001\u0000\u0000\u0000\u00c9\u00c7"+
		"\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005\u000f\u0000\u0000\u00cb\u00d0"+
		"\u0005!\u0000\u0000\u00cc\u00cd\u0005\u0010\u0000\u0000\u00cd\u00cf\u0005"+
		"!\u0000\u0000\u00ce\u00cc\u0001\u0000\u0000\u0000\u00cf\u00d2\u0001\u0000"+
		"\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d0\u00d1\u0001\u0000"+
		"\u0000\u0000\u00d13\u0001\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000"+
		"\u0000\u00d3\u00d4\u0005\u0015\u0000\u0000\u00d4\u00d9\u0005\u001a\u0000"+
		"\u0000\u00d5\u00d6\u0005\u0010\u0000\u0000\u00d6\u00d8\u0005\u001a\u0000"+
		"\u0000\u00d7\u00d5\u0001\u0000\u0000\u0000\u00d8\u00db\u0001\u0000\u0000"+
		"\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00d9\u00da\u0001\u0000\u0000"+
		"\u0000\u00da5\u0001\u0000\u0000\u0000\u00db\u00d9\u0001\u0000\u0000\u0000"+
		"\u00dc\u00dd\u0005\u0016\u0000\u0000\u00dd\u00de\u0005)\u0000\u0000\u00de"+
		"7\u0001\u0000\u0000\u0000\u0012=FXp|\u0083\u0088\u008c\u008e\u009a\u00b2"+
		"\u00b6\u00b9\u00bc\u00bf\u00c7\u00d0\u00d9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
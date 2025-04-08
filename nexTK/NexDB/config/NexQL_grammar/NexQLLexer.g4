lexer grammar NexQLLexer;

// KEYWORDS
// - statement
KW_FIND : 'FIND';
KW_COLLECT : 'COLLECT';
KW_LOAD : 'LOAD';
KW_DELETE : 'DELETE';
KW_CREATE : 'CREATE';
KW_SEARCH : 'SEARCH';
// - substatement
KW_FILTER : 'FILTER';
KW_MATCH : 'MATCH';
KW_WITH : 'WITH';
// - entity types
KW_TAG : 'TAG';
KW_SCHEMA : 'SCHEMA';
KW_SCHEMAS : 'SCHEMAS';
KW_BATCH : 'BATCH';
KW_BATCHES : 'BATCHES';
KW_DATASET : 'DATASET';
KW_DATASETS : 'DATASETS';
KW_COLLECTION : 'COLLECTION';
KW_COLLECTIONS : 'COLLECTIONS';
KW_TOPICS : 'TOPICS';
KW_TOPIC : 'TOPIC';
// - properties
KW_COLUMN : 'COLUMN';
KW_CONSTANT : 'CONSTANT';
KW_INFO : 'INFO';
KW_TYPE : 'TYPE';
KW_SUBSCHEMA : 'SUBSCHEMA';
KW_SIZE : 'SIZE';
KW_CREATED : 'CREATED';
// - options / flags
KW_DEEP : 'DEEP';
KW_SHOW : 'SHOW';
KW_PAGINATE : 'PAGINATE';
KW_PAGE : 'PAGE';
// - other
KW_IN : 'IN';
KW_AS : 'AS';
KW_FOR : 'FOR';
KW_FROM : 'FROM';


// built-in identifiers
BI_SHOW_ONLY_PROPERTY :  'BATCH_INFO' | 'SCHEMA_INFO' | 'COLUMNS' | 'CONSTANTS';

// Value literals
LI_FLOAT : F_FLOAT;
LI_INT : F_INTEGER;
LI_WILDCARD_STRING : '"' F_FREE_STRING '*"';
LI_STRING : '"' F_FREE_STRING '"';
LI_DATATYPE : 'STRING' | 'INT' | 'FLOAT' | 'TIMESTAMP';

// OPERATORS
OP_EQUALS : '=';
OP_COMPARISON_NO_EQUALS : '!=' | '<' | '>' | '<=' | '>=';
OP_OR : 'OR';
OP_ARROW : '->';
OP_COMMA : ',';

// Identifiers
ID_NAME : F_SNAKE_CASE_STRING; // actual
ID_UUID : F_UUID; // actual
// ID_NAME : '_name_'; // debug
// ID_UUID : '_uuid_'; // debug

fragment F_FREE_STRING : ~["\r\n]*;
fragment F_SNAKE_CASE_STRING : [a-z] [a-zA-Z0-9_]*;
fragment F_X : [0-9a-f];
fragment F_X4 : F_X F_X F_X F_X;
fragment F_UUID : F_X4 F_X4 '-' F_X4 '-' F_X4 '-' F_X4 '-' F_X4 F_X4 F_X4;
fragment F_INTEGER : [0-9]+;
fragment F_FLOAT : [0-9]+ '.' [0-9]+;

SKIP_WS : [ \t\r\n]+ -> skip;
SKIP_COMMENT : '--' ~[\r\n]* -> skip;

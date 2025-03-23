lexer grammar QueryLanguageLexer;

// KEYWORDS
// - statement
KW_FIND : 'FIND';
KW_COLLECT : 'COLLECT';
KW_LOAD : 'LOAD';
KW_DELETE : 'DELETE';
KW_CREATE : 'CREATE';
// - substatement
KW_FILTER : 'FILTER';
KW_MATCH : 'MATCH';
// - entity types
KW_TAG : 'TAG';
KW_SCHEMA : 'SCHEMA';
KW_BATCH : 'BATCH';
KW_DATASET : 'DATASET';
KW_COLLECTION : 'COLLECTION';
// - properties
KW_COLUMN : 'COLUMN';
KW_CONSTANT : 'CONSTANT';
KW_INFO : 'INFO';
KW_TYPE : 'TYPE';
// - options / flags
KW_DEEP : 'DEEP';
KW_LIMIT : 'LIMIT';
KW_SHOW : 'SHOW';
// - other
KW_IN : 'IN';
KW_AS : 'AS';
KW_FOR : 'FOR';
KW_FROM : 'FROM';

// built-in identifiers
BI_ENTITY_TYPE : KW_SCHEMA | KW_DATASET | KW_BATCH | KW_COLLECTION | KW_TAG;
BI_ENTITY_TYPE_PLURAL : 'SCHEMAS' | 'DATASETS' | 'BATCHES' | 'COLLECTIONS' | 'TAGS';
BI_FILTERABLE_PROPERTY : 'SIZE' | 'CREATED';
BI_SHOWABLE_PROPERTY : BI_FILTERABLE_PROPERTY | 'BATCH_INFO' | 'SCHEMA_INFO' | BI_ENTITY_TYPE | 'COLUMNS' | 'CONSTANTS';

// Value literals
LI_VALUE : LI_STRING | F_FLOAT | F_INTEGER;
LI_INT : F_INTEGER;
LI_WILDCARD_STRING : '\'' F_FREE_STRING ('*')? '\'';
LI_STRING : '\'' F_FREE_STRING '\'';
LI_DATATYPE : 'STRING' | 'INT' | 'FLOAT' | 'TIMESTAMP';

// OPERATORS
OP_COMPARISON : OP_EQUALS | '!=' | '<' | '>' | '<=' | '>=';
OP_UNION : 'AND' | 'OR' | 'NOT';
OP_ARROW : '->';
OP_COMMA : ',';
OP_EQUALS : '=';

// Identifiers
// ID_NAME : SNAKE_CASE_STRING; // actual
// ID_UUID : UUID; // actual
ID_NAME : '_name_'; // debug
ID_UUID : '_uuid_'; // debug

fragment F_FREE_STRING : [ -~]*;
fragment F_SNAKE_CASE_STRING : [a-z] [a-zA-Z0-9_]*;
fragment F_X : [0-9a-f];
fragment F_X4 : F_X F_X F_X F_X;
fragment F_UUID : F_X4 F_X4 '-' F_X4 '-' F_X4 '-' F_X4 '-' F_X4 F_X4 F_X4;
fragment F_INTEGER : [0-9]+;
fragment F_FLOAT : [0-9]+ '.' [0-9]+;

SKIP_WS : [ \t\r\n]+ -> skip;
SKIP_COMMENT : '--' ~[\r\n]* -> skip;

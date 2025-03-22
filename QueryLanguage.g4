grammar QueryLanguage;

query : findstatement | collectstatement | loadstatement | createstatement | deletestatement;

findstatement : 'FIND' ENTITY_TYPE_PLURAL discovery_clause result_specifiers;
collectstatement : 'COLLECT' ( 'DEEP' )? SCHEMA_IDENTIFIER discovery_clause_with_match 'AS' COLLECTION_IDENTIFIER;
loadstatement : 'LOAD' DATASET_IDENTIFIER result_specifiers;
deletestatement : 'DELETE' UUID;
createstatement : create_tag_key_statement | create_tag_value_statement | create_schema_statement | create_collection_statement;

create_tag_key_statement : 'CREATE' 'TAG' TAG_IDENTIFIER;
create_tag_value_statement : 'CREATE' 'TAG' TAG_IDENTIFIER 'FOR' TAG_IDENTIFIER;
create_schema_statement : 'CREATE' 'SCHEMA' SCHEMA_IDENTIFIER schema_body;
create_collection_statement : 'CREATE' 'COLLECTION' 'FROM' COLLECTION_IDENTIFIER;

schema_body : ( 'INFO' STRING_LITERAL )? 'COLUMNS' fields_defenition 'CONSTANTS' fields_defenition;
fields_defenition : field_defenition ( ',' field_defenition )*;
field_defenition : IDENTIFIER DATATYPE;

discovery_clause : ( collection_include_clause )? filter_clause;
discovery_clause_with_match : ( collection_include_clause )? (filter_clause | match_clause)*;
collection_include_clause : 'IN' collection_expression;
filter_clause : 'FILTER' filter_condition;
filter_condition : property_name_filter_condition | property_value_filter_condition | tag_filter_condition;
property_name_filter_condition : ENTITY_TYPE '=' WILDCARD_STRING_LITERAL;
property_value_filter_condition : FILTERABLE_PROPERTY COMPARISON_OPERATOR LITERAL_VALUE;
tag_filter_condition : IDENTIFIER '=' IDENTIFIER;
match_clause : 'MATCH' CONSTANT_IDENTIFIER COMPARISON_OPERATOR LITERAL_VALUE;

collection_expression : COLLECTION_IDENTIFIER ( UNION_OPERATOR COLLECTION_IDENTIFIER )*;
result_specifiers : ( columns_specifier )? ( constants_specifier )? ( show_specifier )? ( limit_specifier )?;

columns_specifier : 'COLUMNS' IDENTIFIER ( ',' IDENTIFIER )*;
constants_specifier : 'CONSTANTS' IDENTIFIER ( ',' IDENTIFIER )*;
show_specifier : 'SHOW' SHOWABLE_PROPERTY ( ',' SHOWABLE_PROPERTY )*;
limit_specifier : 'LIMIT' NUMBER;

ENTITY_TYPE : 'SCHEMA' | 'DATASET' | 'BATCH' | 'COLLECTION' | 'TAG';
ENTITY_TYPE_PLURAL : 'SCHEMAS' | 'DATASETS' | 'BATCHES' | 'COLLECTIONS' | 'TAGS';
FILTERABLE_PROPERTY : 'SIZE' | 'CREATED';
SHOWABLE_PROPERTY : FILTERABLE_PROPERTY | 'BATCH_INFO' | 'SCHEMA_INFO' | ENTITY_TYPE;
COLLECTION_IDENTIFIER : IDENTIFIER;
SCHEMA_IDENTIFIER : IDENTIFIER;
TAG_IDENTIFIER : IDENTIFIER;
CONSTANT_IDENTIFIER : IDENTIFIER ( '->' IDENTIFIER )*;
BATCH_IDENTIFIER : IDENTIFIER;
DATASET_IDENTIFIER : UUID | ( BATCH_IDENTIFIER IDENTIFIER );
IDENTIFIER : UUID | SNAKE_CASE_STRING;
LITERAL_VALUE : STRING_LITERAL | NUMBER;
WILDCARD_STRING_LITERAL : '\'' CHARACTER+ ('*')? '\'';
STRING_LITERAL : '\'' CHARACTER+ '\'';
DATATYPE : 'STRING';
COMPARISON_OPERATOR : '=' | '!=' | '<' | '>' | '<=' | '>=';
UNION_OPERATOR : 'AND' | 'OR' | 'NOT';

fragment CHARACTER : [a-zA-Z0-9_];
fragment SNAKE_CASE_STRING : [a-z] [a-zA-Z0-9_]*;
UUID : [0-9a-fA-F]{8}'-'[0-9a-fA-F]{4}'-'[0-9a-fA-F]{4}'-'[0-9a-fA-F]{4}'-'[0-9a-fA-F]{12};
NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;

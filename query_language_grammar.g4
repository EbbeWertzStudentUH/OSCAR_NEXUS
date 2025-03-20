grammar FindQuery;

// Parser Rules
query         : 'FIND' schema_name root? columns? constants? filter* match* subschema* ;
schema_name   : IDENTIFIER ;
root          : 'ROOT' ;
columns       : 'COLUMNS' (IDENTIFIER (',' IDENTIFIER)*) | '*' ;
constants     : 'CONSTANTS' (IDENTIFIER (',' IDENTIFIER)*) | '*' ;
filter        : 'FILTER' prop_expression ;
match         : 'MATCH' const_expression ;
subschema     : 'SUBSCHEMA' IDENTIFIER ;

prop_expression  : property comparator value ;
const_expression : constant_name comparator value ;

property      : 'dataset_size' | 'dataset_name' | 'dataset_uuid' | 'dataset_uploaded' ;
comparator    : '==' | '!=' | '<' | '>' | '<=' | '>=' ;
value         : STRING | NUMBER | TIMESTAMP ;
constant_name : IDENTIFIER ('.' IDENTIFIER)* ;  // Nested constants

// Lexer Rules
IDENTIFIER    : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING        : '"' (~["])* '"' ;
NUMBER        : [0-9]+ ('.' [0-9]+)? ;
TIMESTAMP     : DIGIT+ '-' DIGIT+ '-' DIGIT+ 'T' DIGIT+ ':' DIGIT+ ':' DIGIT+ 'Z' ;
DIGIT         : [0-9] ;
WS            : [ \t\r\n]+ -> skip ;  // Ignore whitespace

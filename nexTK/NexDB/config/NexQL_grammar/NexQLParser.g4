parser grammar NexQLParser;

options { tokenVocab=NexQLLexer; }
queries : query+ EOF;
query : KW_FIND (entity_type=BI_ENTITY_TYPE_PLURAL | topic=id_simple) (KW_IN collection=id_simple)? show=show_specifier? limit=limit_specifier? #query_find
      | KW_COLLECT deep=KW_DEEP? id=id_simple filters+=filter_condition* matches+=match_condition* KW_AS name=ID_NAME #query_collect
      | KW_CREATE body=create_body #query_create
      | KW_DELETE type=bi_entity_type id=ID_UUID #query_delete
      | KW_TOPICS #query_listTopics;

// CREATE
create_body : KW_TAG name=ID_NAME #create_tag_key
            | KW_TAG name=ID_NAME KW_FOR keyId=id_simple #create_tag_value
            | KW_COLLECTION KW_FROM name=ID_NAME #create_collection
            | KW_SCHEMA name=ID_NAME KW_INFO info=LI_STRING fields+=field_assignment (OP_COMMA fields+=field_assignment)* #create_schema;

field_assignment : fieldType=(KW_COLUMN | KW_CONSTANT) name=ID_NAME KW_TYPE type=LI_DATATYPE;

// DISCOVERY
value_literals : values+=li_value (OP_OR values+=li_value)*;
identifier_literals : wildcardName=LI_WILDCARD_STRING | (id_literal (OP_OR id_literal)*);
filter_condition : KW_FILTER not=OP_NOT? type=bi_entity_type OP_EQUALS identifier_literals #property_name_filter
                 | KW_FILTER not=OP_NOT? prop=BI_FILTERABLE_PROPERTY operator=op_comparison value=value_literals #property_value_filter
                 | KW_FILTER not=OP_NOT? tagKey=id_simple OP_EQUALS tagValues=identifier_literals #tag_filter;

match_condition : KW_MATCH (nestedName=deep_nested_identifier | id=ID_UUID) operator=op_comparison value=li_value;

show_specifier : KW_SHOW properties+=bi_showable_property (OP_COMMA properties+=bi_showable_property)*;
limit_specifier : KW_LIMIT amount=LI_INT;

nested_identifier : root_identifier=id_simple OP_ARROW sub_identifier=id_simple;

deep_nested_identifier : identifier_chain+=ID_NAME (OP_ARROW identifier_chain+=ID_NAME)*;


// parsed lexer tokens
id_simple : identifier=ID_UUID #id_uuid | identifier=ID_NAME #id_name;
id_literal : identifier=ID_UUID #li_uuid | identifier=LI_STRING #li_name;
bi_entity_type : KW_SCHEMA | KW_DATASET | KW_BATCH;
bi_showable_property : BI_FILTERABLE_PROPERTY | KW_SCHEMA | KW_DATASET | KW_BATCH | KW_TAG | BI_SHOW_ONLY_PROPERTY;
li_value : LI_FLOAT | LI_INT | LI_STRING;
op_comparison : OP_COMPARISON_NO_EQUALS | OP_EQUALS;

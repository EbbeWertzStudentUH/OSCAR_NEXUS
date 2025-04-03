parser grammar NexQLParser;

options { tokenVocab=NexQLLexer; }
queries : query+ EOF;
query : KW_FIND (entity_type=BI_ENTITY_TYPE_PLURAL | topic=id_simple) (KW_IN collection=id_simple)? filters+=filter_condition* show=show_specifier? paginate=pagination_specifier? #query_find
      | KW_COLLECT deep=KW_DEEP? identifier=id_simple filters+=filter_condition* matches+=match_condition* KW_AS name=ID_NAME #query_collect
      | KW_CREATE body=create_body #query_create
      | KW_DELETE entity_type=bi_deletable_entity_type uuid=ID_UUID #query_delete
      | KW_TOPICS #query_listTopics;

// CREATE (Batch and dataset are not to create)
create_body : KW_TOPIC name=ID_NAME #create_tag_key
            | KW_TAG name=ID_NAME KW_FOR keyId=id_simple #create_tag_value
            | KW_COLLECTION KW_FROM name=ID_NAME #create_collection
            | KW_SCHEMA name=ID_NAME KW_INFO info=LI_STRING fields+=field_assignment* subs+=subschema_assignment* #create_schema;

field_assignment : fieldType=(KW_COLUMN | KW_CONSTANT) name=ID_NAME KW_TYPE data_type=LI_DATATYPE;
subschema_assignment : KW_SUBSCHEMA name=ID_NAME KW_SCHEMA sub_schema=id_simple ;

// DISCOVERY
value_literals : values+=li_value (OP_OR values+=li_value)*;
identifier_literals : wildcard_name=LI_WILDCARD_STRING | (identifiers+=id_literal (OP_OR identifiers+=id_literal)*);
filter_condition : KW_FILTER entity_type=bi_filterable_entity_type OP_EQUALS identifiers=identifier_literals #property_name_filter
                 | KW_FILTER prop=BI_FILTERABLE_PROPERTY operator=op_comparison value=value_literals #property_value_filter
                 | KW_FILTER tagKey=id_simple OP_EQUALS tagValues=identifier_literals #tag_filter;

match_condition : KW_MATCH (nestedName=nested_name_identifier | uuid=ID_UUID) operator=op_comparison value=li_value;

show_specifier : KW_SHOW properties+=bi_showable_property (OP_COMMA properties+=bi_showable_property)*;
pagination_specifier : KW_PAGINATE amount=LI_INT KW_PAGE page=LI_INT;

nested_name_identifier : identifier_chain+=ID_NAME (OP_ARROW identifier_chain+=ID_NAME)*;


// parsed lexer tokens
id_simple : identifier=ID_UUID #id_uuid | identifier=ID_NAME #id_name;
id_literal : identifier=ID_UUID #li_uuid | identifier=LI_STRING #li_name;
bi_filterable_entity_type : entity_type=(KW_SCHEMA | KW_DATASET | KW_BATCH);
bi_deletable_entity_type : entity_type=(KW_SCHEMA | KW_DATASET | KW_BATCH | KW_TAG | KW_TOPIC);
bi_showable_property : BI_FILTERABLE_PROPERTY | KW_SCHEMA | KW_DATASET | KW_BATCH | KW_TAG | BI_SHOW_ONLY_PROPERTY;
li_value : val_fl=LI_FLOAT | val_int=LI_INT | val_str=LI_STRING;
op_comparison : operator=(OP_COMPARISON_NO_EQUALS | OP_EQUALS);

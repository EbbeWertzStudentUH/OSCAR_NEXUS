parser grammar NexQLParser;

options { tokenVocab=NexQLLexer; }
queries : query+ EOF;
query : KW_FIND (entity_type=bi_findable_entity_type | topic=id_simple) (KW_IN collection=id_simple)? filters+=filter_condition* /*show=show_specifier? paginate=pagination_specifier?*/ #query_find
      | KW_COLLECT /*deep=KW_DEEP?*/ identifier=id_simple filters+=filter_condition* matches+=with_condition* KW_AS name=ID_NAME #query_collect
      | KW_SEARCH (entity_type=bi_searchable_entity_type | topic=id_simple) (KW_MATCH match_literals=identifier_literals)? #query_search
      | KW_CREATE body=create_body #query_create
      | KW_DELETE entity_type=bi_deletable_entity_type uuid=ID_UUID #query_delete
      | KW_TOPICS #query_listTopics;

// CREATE (Batch and dataset are not to create)
create_body : KW_TOPIC name=ID_NAME #create_tag_key
            | KW_TAG name=ID_NAME KW_FOR keyId=id_simple #create_tag_value
            | KW_COLLECTION name=ID_NAME KW_FROM existing_collect_name=ID_NAME #create_collection
            | KW_SCHEMA name=ID_NAME KW_INFO info=LI_STRING fields+=field_assignment* subs+=subschema_assignment* #create_schema;

field_assignment : fieldType=(KW_COLUMN | KW_CONSTANT) name=ID_NAME KW_TYPE data_type=LI_DATATYPE;
subschema_assignment : KW_SUBSCHEMA name=ID_NAME KW_SCHEMA sub_schema=id_simple ;

// DISCOVERY
value_literals : values+=li_value (OP_OR values+=li_value)*;
identifier_literals : wildcard_name=LI_WILDCARD_STRING | (identifiers+=id_literal (OP_OR identifiers+=id_literal)*);
filter_condition : KW_FILTER entity_type=bi_filterable_entity_type OP_EQUALS identifiers=identifier_literals #name_filter
                 | KW_FILTER prop=bi_filterable_property operator=op_comparison value=value_literals #property_filter
                 | KW_FILTER tagKey=id_simple OP_EQUALS tagValues=identifier_literals #tag_filter;

with_condition : KW_WITH (nestedName=nested_name_identifier | uuid=ID_UUID) operator=op_comparison value=li_value;

pagination_specifier : KW_PAGINATE amount=LI_INT KW_PAGE page=LI_INT;

nested_name_identifier : identifier_chain+=ID_NAME (OP_ARROW identifier_chain+=ID_NAME)*;


// parsed lexer tokens
id_simple : identifier=ID_UUID #id_uuid | identifier=ID_NAME #id_name;
id_literal : identifier=ID_UUID #li_uuid | identifier=LI_STRING #li_name;

bi_findable_entity_type : entity_type=(KW_SCHEMAS | KW_DATASETS | KW_BATCHES);
bi_filterable_entity_type : entity_type=(KW_SCHEMA | KW_DATASET | KW_BATCH);
bi_deletable_entity_type : entity_type=(KW_SCHEMA | KW_DATASET | KW_BATCH | KW_TAG | KW_TOPIC);
bi_searchable_entity_type : entity_type=(KW_SCHEMAS | KW_DATASETS | KW_BATCHES | KW_TOPICS | KW_COLLECTIONS);

bi_filterable_property : prop=(KW_SIZE | KW_CREATED);

li_value : val_fl=LI_FLOAT | val_int=LI_INT | val_str=LI_STRING;
op_comparison : operator=(OP_COMPARISON_NO_EQUALS | OP_EQUALS);

parser grammar NexQLParser;

options { tokenVocab=NexQLLexer; }

query : KW_FIND type=BI_ENTITY_TYPE_PLURAL discover=discovery_clause show=show_specifier? limit=limit_specifier? #find
      | KW_COLLECT deep=KW_DEEP? id=simple_identifier discover=discovery_clause_with_match KW_AS name=ID_NAME #collect
      | KW_CREATE body=create_body #create
      | KW_DELETE type=BI_ENTITY_TYPE id=ID_UUID #delete;

// CREATE
create_body : KW_TAG name=ID_NAME #create_tag_key
            | KW_TAG name=ID_NAME KW_FOR keyId=simple_identifier #create_tag_value
            | KW_COLLECTION KW_FROM name=ID_NAME #create_collection
            | KW_SCHEMA name=ID_NAME KW_INFO info=LI_STRING fields+=field_assignment (OP_COMMA fields+=field_assignment)* #create_schema;

field_assignment : fieldType=(KW_COLUMN | KW_CONSTANT) name=ID_NAME KW_TYPE type=LI_DATATYPE;

// DISCOVERY
discovery_clause : collect=collection_condition? filters+=filter_condition*;

discovery_clause_with_match : collect=collection_condition? filters+=filter_condition* matches+=match_condition*;

collection_condition : KW_IN collectionIds+=simple_identifier (OP_UNION collectionIds+=simple_identifier)*;

filter_condition : KW_FILTER type=BI_ENTITY_TYPE OP_EQUALS (name=LI_WILDCARD_STRING | id=ID_UUID) #property_name_filter
                 | KW_FILTER prop=BI_FILTERABLE_PROPERTY operator=OP_COMPARISON value=LI_VALUE #property_value_filter
                 | KW_FILTER tagKey=simple_identifier OP_EQUALS tagValue=simple_identifier #tag_filter;

match_condition : KW_MATCH id=deep_nested_identifier operator=OP_COMPARISON value=LI_VALUE;

show_specifier : KW_SHOW properties+=BI_SHOWABLE_PROPERTY (OP_COMMA properties+=BI_SHOWABLE_PROPERTY)*;
limit_specifier : KW_LIMIT amount=LI_INT;

simple_identifier : identifier=ID_UUID #uuid | identifier=ID_NAME #name;

nested_identifier : root_identifier=simple_identifier OP_ARROW sub_identifier=simple_identifier;

deep_nested_identifier : identifier_chain+=simple_identifier (OP_ARROW identifier_chain+=simple_identifier)*;

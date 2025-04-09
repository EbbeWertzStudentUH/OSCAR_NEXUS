from dataclasses import dataclass

from config.antlr_generated.NexQLParser import NexQLParser
from query_models.reading_helper_models import SimpleId, Filters, SimpleFilterCondition, IdentifierLiterals
from util import entity_to_class_name


@dataclass
class FindQuery: # FIND ...
    select_class:str
    collection:SimpleId | None
    filters:Filters

    @classmethod
    def from_context(cls, ctx:NexQLParser.Query_findContext):
        entity_type, topic, collection, filters_ctx = ctx.entity_type, ctx.topic, ctx.collection, ctx.filters
        select_class = entity_to_class_name(entity_type.entity_type.text) if entity_type else "Tag"
        collection_filter = SimpleId.from_context(collection) if collection else None
        filters = Filters.from_contexts(filters_ctx)

        if topic:
            simple_id = SimpleId.from_context(topic)
            filters.simple_filters.append(SimpleFilterCondition.from_simple_id(simple_id, "TagKey"))

        return cls(select_class, collection_filter, filters)

@dataclass
class CollectQuery:
    schema:SimpleId
    filters: Filters
    save_name: str

    @classmethod
    def from_context(cls, ctx: NexQLParser.Query_collectContext):
        schema_id_ctx, filters_ctx, data_filters_ctx, name_ctx = ctx.schema_id, ctx.filters, ctx.data_filters, ctx.name
        schema = SimpleId.from_context(schema_id_ctx)
        filters = Filters.from_contexts(filters_ctx, data_filters_ctx)
        return cls(schema, filters, name_ctx.text)

@dataclass
class SearchQuery:
    select_class: str
    simple_filters: list[SimpleFilterCondition]

    @classmethod
    def from_context(cls, ctx: NexQLParser.Query_searchContext):
        entity_type_ctx, topic_ctx, match_literals_ctx = ctx.entity_type, ctx.topic, ctx.match_literals
        select_class = entity_to_class_name(entity_type_ctx.entity_type.text) if entity_type_ctx else "Tag"
        id_literals = IdentifierLiterals.from_context(match_literals_ctx) if match_literals_ctx else None
        simple_filters = []
        if id_literals:
            simple_filters.append(SimpleFilterCondition.from_id_literals(id_literals, select_class))
        if topic_ctx:
            simple_id = SimpleId.from_context(topic_ctx)
            simple_filters.append(SimpleFilterCondition.from_simple_id(simple_id, "TagKey"))

        return cls(select_class, simple_filters)
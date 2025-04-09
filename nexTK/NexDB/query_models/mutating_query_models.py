from dataclasses import dataclass
from typing import Literal, List

from config.antlr_generated.NexQLParser import NexQLParser
from query_models.helper_query_models import SimpleFilterCondition, SimpleId


@dataclass
class TagTopicCreateQuery:
    name:str

    @classmethod
    def from_context(cls, ctx:NexQLParser.Create_tag_keyContext):
        return cls(ctx.name.text)

@dataclass
class TagCreateQuery:
    name:str
    key_id:SimpleId

    @classmethod
    def from_context(cls, ctx: NexQLParser.Create_tag_valueContext):
        key_id = SimpleId.from_context(ctx.key_filter)
        return cls(ctx.name.text, key_id)

@dataclass
class CollectionCreateQuery:
    save_name:str
    from_name:str

    @classmethod
    def from_context(cls, ctx: NexQLParser.Create_collectionContext):
        return cls(ctx.name.text, ctx.existing_collect_name.text)

@dataclass
class FieldCreateQuery:
    is_constant:bool
    name:str
    data_type:str

    @classmethod
    def from_context(cls, ctx: NexQLParser.Field_assignmentContext):
        is_constant = ctx.field_type.text == 'CONSTANT'
        return cls(is_constant, ctx.name.text, ctx.data_type.text)

@dataclass
class SubSchemaFieldCreateQuery:
    name: str
    schema_id: SimpleId

    @classmethod
    def from_context(cls, ctx: NexQLParser.Subschema_assignmentContext):
        subs_id = SimpleId.from_context(ctx.sub_schema)
        return cls(ctx.name.text,subs_id)

@dataclass
class SchemaCreateQuery:
    name:str
    info:str
    fields:list[FieldCreateQuery]
    sub_schemas:list[SubSchemaFieldCreateQuery]

    @classmethod
    def from_context(cls, ctx: NexQLParser.Create_schemaContext):
        name_ctx, info_ctx, fields_ctx, subs_ctx = ctx.name, ctx.info, ctx.fields, ctx.subs
        name, info = name_ctx.text, info_ctx.text.strip('"')
        fields = [FieldCreateQuery.from_context(f) for f in fields_ctx]
        subs = [SubSchemaFieldCreateQuery.from_context(s) for s in subs_ctx]
        return cls(name, info, fields, subs)
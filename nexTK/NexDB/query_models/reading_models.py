from dataclasses import dataclass
from typing import Any, Literal
from uuid import UUID
from config.antlr_generated.NexQLParser import NexQLParser
from db.models import Tag
from util import entity_to_class_name, prop_to_field

@dataclass
class SimpleId: # ID_NAME or ID_UUID
    field:Literal['name', 'id']
    value:str|UUID

    @classmethod
    def from_context(cls, ctx:NexQLParser.Id_simpleContext):
        if isinstance(ctx, NexQLParser.Id_uuidContext):
            return cls('id', UUID(ctx.identifier.text))
        elif isinstance(ctx, NexQLParser.Id_nameContext):
            return cls('name', ctx.identifier.text)

@dataclass
class LiteralId: # ID_NAME or ID_UUID
    field:Literal['name', 'id']
    value:str|UUID

    @classmethod
    def from_context(cls, ctx:NexQLParser.Id_literalContext):
        if isinstance(ctx, NexQLParser.Li_uuidContext):
            return cls('id', UUID(ctx.identifier.text))
        elif isinstance(ctx, NexQLParser.Li_nameContext):
            return cls('name', ctx.identifier.text.strip('"'))

@dataclass
class IdentifierLiterals:
    field:str
    values:list[str|UUID]
    is_wildcard:bool
    @classmethod
    def from_context(cls, ctx: NexQLParser.Identifier_literalsContext):
        if ctx.wildcard_name:
            wildcard:str = ctx.wildcard_name.text.strip('"')[:-1] + "%"
            return cls("name", [wildcard], True)

        field = ''
        values = []
        for id_literal_ctx in ctx.identifiers:
            id_literal = LiteralId.from_context(id_literal_ctx)
            if field and field != id_literal.field:
                raise ValueError("List of identifiers cannot be of mixed type. Use either all UUIDs or all names")
            field = id_literal.field
            values.append(id_literal.value)
        return cls(field, values, False)

@dataclass
class ValueLiteral:
    value: float|int|str

    @classmethod
    def from_context(cls, ctx: NexQLParser.Li_valueContext):
        if ctx.val_fl:
            return cls(float(ctx.val_fl.text))
        if ctx.val_int:
            return cls(int(ctx.val_int.text))
        if ctx.val_str:
            return cls(ctx.val_str.text.strip('"'))

@dataclass
class ValueLiterals:
    values: list[ValueLiteral]

    @classmethod
    def from_context(cls, ctx: NexQLParser.Value_literalsContext):
        return cls([ValueLiteral.from_context(value) for value in ctx.values])

@dataclass
class SimpleFilterCondition: # FILTER ...
    source_class:str
    source_field:str
    operator:str
    value:Any

    @classmethod
    def from_simple_id(cls, simple_id:SimpleId, entity_class:str):
        return cls(entity_class, simple_id.field, '=', simple_id.value)

    @classmethod
    def from_literal_id(cls, literal_id:LiteralId, entity_class:str):
        return cls(entity_class, literal_id.field, '=', literal_id.value)

    @classmethod
    def from_prop_filter_context(cls, ctx:NexQLParser.Property_filterContext):
        entity_class, field = prop_to_field(ctx.prop.prop.text)
        value_literals = ValueLiterals.from_context(ctx.value)
        values = [vl.value for vl in value_literals.values]
        operator = 'in' if len(values) > 1 else ctx.operator.operator.text
        if operator == 'in' and ctx.operator.operator.text != '=':
            raise ValueError("Multiple value filter is only supported for the '=' operator")

        if operator != 'in':
            values = values[0]
        return cls(entity_class, field, operator, values)

    @classmethod
    def from_name_filter_context(cls, ctx: NexQLParser.Name_filterContext):
        entity_class = entity_to_class_name(ctx.entity_type.entity_type.text)
        id_literals = IdentifierLiterals.from_context(ctx.identifiers)
        operator = 'ilike' if id_literals.is_wildcard else 'in' if len(id_literals.values) > 1 else '='
        values = id_literals.values if operator == 'in' else id_literals.values[0]
        return cls(entity_class, id_literals.field, operator, values)

@dataclass
class TagFilterCondition: # FILTER ...
    key_field:str
    key_value:str|UUID
    tag_field:str
    tag_value:str|UUID | list[str|UUID]
    operator:str

    @classmethod
    def from_tag_filter_context(cls, ctx: NexQLParser.Tag_filterContext):
        key_simple_id = SimpleId.from_context(ctx.tagKey)
        id_literals = IdentifierLiterals.from_context(ctx.tagValues)
        if id_literals.is_wildcard:
            raise ValueError("Wildcard matching not supported for tags")

        operator = 'in' if len(id_literals.values) > 1 else '='
        values = id_literals.values if operator == 'in' else id_literals.values[0]
        return cls(key_simple_id.field, key_simple_id.value, id_literals.field, values, operator)

@dataclass
class FindQuery: # FIND ...
    select_class:str
    collection:SimpleId
    simple_filters:list[SimpleFilterCondition]
    tag_filters:list[TagFilterCondition]

    @classmethod
    def from_context(cls, ctx:NexQLParser.Query_findContext):
        entity_type, topic, collection, filters_ctx = ctx.entity_type, ctx.topic, ctx.collection, ctx.filters
        select_class = entity_to_class_name(entity_type.entity_type.text) if entity_type else "Tag"
        collection_filter = SimpleId.from_context(collection) if collection else None
        simple_filters, tag_filters = [], []
        if topic:
            simple_id = SimpleId.from_context(topic)
            simple_filters.append(SimpleFilterCondition.from_simple_id(simple_id, "Tag"))

        for filter_ctx in filters_ctx:
            if isinstance(filter_ctx, NexQLParser.Tag_filterContext):
                tag_filters.append(TagFilterCondition.from_tag_filter_context(filter_ctx))
            elif isinstance(filter_ctx, NexQLParser.Property_filterContext):
                simple_filters.append(SimpleFilterCondition.from_prop_filter_context(filter_ctx))
            elif isinstance(filter_ctx, NexQLParser.Name_filterContext):
                simple_filters.append(SimpleFilterCondition.from_name_filter_context(filter_ctx))

        return cls(select_class, collection_filter, simple_filters, tag_filters)
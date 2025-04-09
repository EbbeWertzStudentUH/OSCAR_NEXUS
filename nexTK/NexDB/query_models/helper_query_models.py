from typing import Any, Literal
from uuid import UUID

from dataclasses import dataclass

from config.antlr_generated.NexQLLexer import NexQLLexer
from config.antlr_generated.NexQLParser import NexQLParser
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
        return cls.from_id_literals(id_literals, entity_class)

    @classmethod
    def from_id_literals(cls, id_literals:IdentifierLiterals, entity_class:str):
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
class DeepIdentifier:
    is_name_chain:bool
    name_chain:list[str]
    uuid:UUID|None

    @classmethod
    def from_nested_name_ctx_or_uuid(cls, ctx:NexQLParser.Nested_name_identifierContext, uuid_token:NexQLLexer.ID_UUID):
        if ctx:
            name_chain = [name.text for name in ctx.identifier_chain]
            return cls(True, name_chain, None)
        else:
            return cls(False, [], uuid_token.text)


@dataclass
class DataFilterCondition:
    deep_identifier:DeepIdentifier
    value: ValueLiteral
    operator:str

    @classmethod
    def from_context(cls, ctx:NexQLParser.With_conditionContext):
        nested_name_ctx, uuid_ctx, operator_ctx, value_ctx = ctx.nested_name, ctx.uuid, ctx.operator, ctx.value
        deep_id = DeepIdentifier.from_nested_name_ctx_or_uuid(nested_name_ctx, uuid_ctx)
        value = ValueLiteral.from_context(value_ctx)
        return cls(deep_id, value, operator_ctx.operator.text)


@dataclass
class Filters:
    simple_filters: list[SimpleFilterCondition]
    tag_filters: list[TagFilterCondition]
    data_filters: list[DataFilterCondition]

    @classmethod
    def from_contexts(cls, filter_ctxs:list[NexQLParser.Filter_conditionContext], with_condition_ctxs:list[NexQLParser.With_conditionContext] = []):
        simple_filters, tag_filters, data_filters = [], [], []
        for filter_ctx in filter_ctxs:
            if isinstance(filter_ctx, NexQLParser.Tag_filterContext):
                tag_filters.append(TagFilterCondition.from_tag_filter_context(filter_ctx))
            elif isinstance(filter_ctx, NexQLParser.Property_filterContext):
                simple_filters.append(SimpleFilterCondition.from_prop_filter_context(filter_ctx))
            elif isinstance(filter_ctx, NexQLParser.Name_filterContext):
                simple_filters.append(SimpleFilterCondition.from_name_filter_context(filter_ctx))
        for with_ctx in with_condition_ctxs:
            data_filters.append(DataFilterCondition.from_context(with_ctx))
        return cls(simple_filters, tag_filters, data_filters)
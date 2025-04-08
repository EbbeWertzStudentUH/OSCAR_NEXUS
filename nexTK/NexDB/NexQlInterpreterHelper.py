from multiprocessing import Value
from uuid import UUID
from config.antlr_generated.NexQLParser import NexQLParser
from util import prop_to_field, entity_to_class_name

    
def extract_li_value(ctx: NexQLParser.Li_valueContext) -> float | int | str:
    if ctx.val_fl:
        return float(ctx.val_fl.text)
    if ctx.val_int:
        return int(ctx.val_int.text)
    if ctx.val_str:
        return ctx.val_str.text[1:-1] # slicing to remove quotation marks
    
def extract_id(ctx:NexQLParser.Id_simpleContext | NexQLParser.Id_literalContext) -> tuple[str, object]:
    if isinstance(ctx, NexQLParser.Id_uuidContext) or isinstance(ctx, NexQLParser.Li_uuidContext):
        return "id", UUID(ctx.identifier.text)
    elif isinstance(ctx, NexQLParser.Id_nameContext):
        return "name", ctx.identifier.text
    elif isinstance(ctx, NexQLParser.Li_nameContext):
        return "name", ctx.identifier.text[1:-1] # slicing to remove quotation marks

def extract_value_literals(ctx: NexQLParser.Value_literalsContext) -> list[object]:
    return [extract_li_value(value) for value in ctx.values]

def extract_identifier_literals(ctx: NexQLParser.Identifier_literalsContext) -> tuple[str, list, bool]:
    if ctx.wildcard_name:
        wildcard = ctx.wildcard_name.text[1:-2] + "%" # slicing to remove quotation marks and replace * by %
        return "name", [wildcard], True # field, values, isWildCard
    
    field = None
    values = []
    for id in ctx.identifiers:
        f, val = extract_id(id)
        if field and field != f:
            raise ValueError("List of identifiers cannot be of mixed type. Use either all UUIDs or all names")
        field = f
        values.append(val)
    
    return field, values, False # field, values, isWildCard

def extract_filter_condition(ctx: NexQLParser.Filter_conditionContext) -> tuple[bool, (tuple[type, str, list|object, str] | tuple[str, object, str, list|object, str])]:
    if isinstance(ctx, NexQLParser.Property_name_filterContext):
        model =entity_to_class_name(ctx.entity_type.entity_type.text)
        field, values, isWildCard = extract_identifier_literals(ctx.identifiers)
        operator = 'ilike' if isWildCard else 'in' if len(values) > 1 else '='
        if operator != 'in':values = values[0]            
        return False, (model, field, values, operator) # isTagFilter, (model_class, field, values, operator)
    elif isinstance(ctx, NexQLParser.Property_value_filterContext):
        model, field = prop_to_field(ctx.prop.text)
        values = extract_value_literals(ctx.value)
        if len(values) > 1 and ctx.operator.operator.text != '=':
            raise ValueError("Multiple value filter is only supported for the '=' operator")
        operator = 'in' if len(values) > 1 else ctx.operator.operator.text
        if operator != 'in':values = values[0]
        return False, (model, field, values, operator) # isTagFilter, (model_class, field, values, operator)
    elif isinstance(ctx, NexQLParser.Tag_filterContext):
        tag_key_f, tag_key_val = extract_id(ctx.tagKey)
        tag_field, tag_values, isWildCard = extract_identifier_literals(ctx.tagValues)
        if isWildCard:
            raise ValueError("Wildcard matching not supported for tags")
        operator = 'in' if len(tag_values) > 1 else '='
        if operator != 'in':tag_values = tag_values[0]
        return True, (tag_key_f, tag_key_val, tag_field, tag_values, operator) # isTagFilter, (key_field, key_value, tag_field, tag_values, operator)
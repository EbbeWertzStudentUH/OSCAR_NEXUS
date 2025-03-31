from uuid import UUID
from config.antlr_generated.NexQLParser import NexQLParser

    
def extract_li_value(ctx: NexQLParser.Li_valueContext) -> float | int | str:
    if ctx.val_fl:
        return float(ctx.val_fl.text)
    if ctx.val_int:
        return int(ctx.val_int.text)
    if ctx.val_str:
        return ctx.val_int.text[1:-1] # slicing to remove quotation marks
    
def extract_id(ctx:NexQLParser.Id_simpleContext | NexQLParser.Id_literalContext) -> tuple[str, object]:
    if isinstance(ctx, NexQLParser.Id_uuidContext) or isinstance(ctx, NexQLParser.Li_uuidContext):
        return "id", UUID(ctx.identifier.text)
    elif isinstance(ctx, NexQLParser.Id_nameContext):
        return "name", ctx.identifier.text
    elif isinstance(ctx, NexQLParser.Li_nameContext):
        return "name", ctx.identifier.text[1:-1] # slicing to remove quotation marks

def extract_value_literals(ctx: NexQLParser.Value_literalsContext) -> tuple[list[object], bool]:
    values = [extract_li_value(value) for value in ctx.values]
    return values, len(values) > 1 # values, isMultiple

def extract_identifier_literals(ctx: NexQLParser.Identifier_literalsContext) -> list[str]:
    if ctx.wildcard_name:
        whildcard = ctx.wildcard_name.text[1:-2] + "%" # slicing to remove quotation marks and replace * by %
        return [("name", whildcard)], False, True # literal, isMultiple, isWildCard
    
    ids = [extract_id(id) for id in ctx.identifiers]
    return ids, len(ids) > 1, False # values, isMultiple, isWildCard
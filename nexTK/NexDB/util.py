import operator
from db.models import Batch, Dataset, Schema, Tag, TagKey

def pl_entity_name_class(name:str) -> type:
    return {"SCHEMAS": Schema,
            "DATASETS": Dataset,
            "BATCHES": Batch}[name]

def si_entity_name_to_class(name:str) -> type:
    return {"SCHEMA": Schema,
            "DATASET": Dataset,
            "BATCH": Batch,
            "TAG": Tag,
            "TOPIC": TagKey}[name]
    
def operator_from_str(string:str):
    return{
        '=': operator.eq,
        '!=': operator.ne,
        '<': operator.lt,
        '>': operator.gt,
        '<=': operator.le,
        '>=': operator.ge,
        'ilike': lambda field, value: field.ilike(value),
        'in': lambda field, value: field.in_(value)}[string]
    
def prop_to_field(prop:str) -> tuple[type, str]:
    return{
        "SIZE": (Dataset, 'size'),
        "CREATED": (Dataset, 'created_at')
    }[prop]
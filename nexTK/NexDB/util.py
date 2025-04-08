import operator


def entity_to_class_name(name:str) -> type:
    return {"SCHEMA": "Schema",
            "SCHEMAS": "Schema",
            "DATASET": "Dataset",
            "DATASETS": "Dataset",
            "BATCH": "Batch",
            "BATCHES": "Batch",
            "COLLECTION": "Collection",
            "COLLECTIONS": "Collection",
            "TOPIC": "TagKey",
            "TOPICS": "TagKey",
            "TAG": "Tag"}[name]
    
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
        "SIZE": ("Dataset", 'size'),
        "CREATED": ("Batch", 'created_at')
    }[prop]
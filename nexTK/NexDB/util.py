import operator
from db.models import Batch, Dataset, Schema
def plural_entity_name_to_model_class(name:str) -> type:
    return {"SCHEMAS": Schema,
            "DATASETS": Dataset,
            "BATCHES": Batch}[name]
    
def operator_from_str(string:str):
    return{
        '=': operator.eq,
        '!=': operator.ne,
        '<': operator.lt,
        '>': operator.gt,
        '<=': operator.le,
        '>=': operator.ge}[string]
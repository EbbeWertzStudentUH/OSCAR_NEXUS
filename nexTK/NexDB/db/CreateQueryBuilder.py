from typing import Literal
from uuid import UUID
from sqlalchemy.orm import Session

from db.models import Schema, Tag, TagKey



class CreateQueryBuilder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._create_class:type = None
        self._name:str = None
        self._extra_data:dict[str, object] = {}
        
    def set_create_class(self, clazz:type):
        self._create_class = clazz
    
    def set_name(self, name:str):
        self._name = name
    
    def set_tag_key(self, field:str, value:UUID | str):
        self._extra_data['key_field'] = field
        self._extra_data['key_value'] = value
    
    def set_schema_info(self, info:str):
        self._extra_data['schema_info'] = info
    
    def add_schema_field(self, field_type:Literal['Col', 'Const'], name:str, datatype:str):
        if 'schema_fields' not in self._extra_data: self._extra_data['schema_fields'] = []
        self._extra_data['schema_fields'].append((field_type, name, datatype))
        
    def build_and_commit(self, session:Session):
        match self._create_class:
            case TagKey.__class__:
                new_item = TagKey(name=self._name)
                session.add(new_item)
            case Tag.__class__:
                key_field_name, key_value = self._extra_data['key_field'], self._extra_data['key_value']
                key_field = getattr(TagKey, key_field_name)
                key = session.query(TagKey.id).filter(key_field == key_value).scalar_subquery()
                new_item = Tag(name=self._name, tag_key_id=key)
                session.add(new_item)
            case Schema.__class__:
                pass
                
                
        
        session.commit()
        
    
    def is_set(self) -> bool:
        return self._create_class is not None
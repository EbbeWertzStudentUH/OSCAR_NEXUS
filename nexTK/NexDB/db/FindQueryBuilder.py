from typing import Callable

from sqlalchemy import and_, func, or_
from db.ImplicitJoiner import ImplicitJoiner
from db.models import Tag, TagKey
from util import operator_from_str
from sqlalchemy.orm import Session



class FindQueryBuilder:
    def __init__(self, Base:type):
        self._joiner = ImplicitJoiner(Base)
        self.reset()
    
    def reset(self):
        self._joiner.reset()
        self._selectClass = None
        self._limit_offset = None
        self._filters = []
        self._tag_filters: list[tuple[tuple[str, object], tuple[str, Callable, list|object]]] = [] # (key_field, key_value), (tag_field, operator, tag_value)
        
    def set_select_class(self, clazz:type):
        self._selectClass = clazz
        self._joiner.set_select_class(clazz)
        
    def add_filter(self, clazz:type, field_name:str, operator_str:str, value):
        if clazz is not self._selectClass:
            self._joiner.add_relation(clazz)
        operator = operator_from_str(operator_str)
        self._filters.append((clazz, field_name, operator, value))
        
    def add_tag_filter(self, key_field:str, key_value:object, tag_field:str, operator_str:str, value:list|object):
        operator = operator_from_str(operator_str)
        self._joiner.add_relation(Tag)
        self._joiner.add_relation(TagKey)
        
        self._tag_filters.append(((key_field, key_value), (tag_field, operator, value)))
        
    def is_set(self) -> bool:
        return self._selectClass is not None
    
    def set_pagination(self, page_size:int, page:int):
        if page <= 0: raise ValueError("Page number must be 1 or higher")
        self._limit_offset = (page_size, page_size*(page-1))
    
    def _build_tag_filter(self, key_tuple: tuple[str, object], tag_tuple: tuple[str, Callable, list|object], key_alias:type, tag_alias:type):
        (key_field, key_value), (tag_field, operator, tag_value) = key_tuple, tag_tuple
        key_att = getattr(key_alias, key_field)
        tag_att = getattr(tag_alias, tag_field)
        key_condition = key_att == key_value
        tag_condition = operator(tag_att, tag_value)
        return and_(key_condition, tag_condition)
        
    def build(self, session:Session):
        
        query = session.query(self._selectClass)
        query, aliasses = self._joiner.build_joins(query)
        
        for (clazz, field_name, operator, value) in self._filters:
            alias = aliasses[clazz] if clazz in aliasses else clazz
            field = getattr(alias, field_name)
            query = query.filter(operator(field, value))
        
        if len(self._tag_filters) > 0:
            key_alias, tag_alias = aliasses[TagKey], aliasses[Tag]
            tag_conditions = [self._build_tag_filter(kt, tt, key_alias, tag_alias) for kt, tt in self._tag_filters]        
            query = query.filter(or_(*tag_conditions))
            query = query.group_by(self._selectClass.id).having(func.count(func.distinct(tag_alias.id)) == len(self._tag_filters))
        
        if self._limit_offset:
            limit, offset = self._limit_offset
            query = query.limit(limit).offset(offset)
            
        return query
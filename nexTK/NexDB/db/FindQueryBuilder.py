from typing import Callable
from db.ImplicitJoiner import ImplicitJoiner
from util import operator_from_str


class FindQueryBuilder:
    def __init__(self, Base:type):
        self._joiner = ImplicitJoiner(Base)
        self._selectClass = None
        self._filters = []
        
    def set_select_class(self, clazz:type):
        self._selectClass = clazz
        self._joiner.set_select_class(clazz)
        
    def add_filter(self, clazz:type, field_name:str, operator_str:str, value):
        self._joiner.add_relation(clazz)
        operator = operator_from_str(operator_str)
        self._filters.append((clazz, field_name, operator, value))
        
    def build(self, session):
        query = session.query(self._selectClass)
        query, aliasses = self._joiner.build_joins(query)
        for (clazz, field_name, operator, value) in self._filters:
            alias = aliasses[clazz]
            field = getattr(alias, field_name)
            query = query.filter(operator(field, value))
        return query
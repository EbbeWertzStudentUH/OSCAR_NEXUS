
from sqlalchemy import and_, or_, func
from sqlalchemy.orm import Session, Query

from db.models import TagKey, Tag, ConstValue, SubSchema, Field, Schema
from query_models.helper_query_models import SimpleFilterCondition, TagFilterCondition, Filters, DataFilterCondition, \
    DeepIdentifier
from util import class_name_to_class, operator_from_str


class FilterQuerierHelper:
    def __init__(self):
        self._session:Session|None = None
        self._collection_schema_id:str|None = None

    def set_session(self, session:Session):
        self._session = session

    def set_collection_schema(self, collection_schema_id:str):
        self._collection_schema_id = collection_schema_id

    @staticmethod
    def _build_simple_filter_condition(filter_condition:SimpleFilterCondition):
        field_class = class_name_to_class(filter_condition.source_class)
        field = getattr(field_class, filter_condition.source_field)
        operator_callable = operator_from_str(filter_condition.operator)
        return operator_callable(field, filter_condition.value)

    @staticmethod
    def _build_tag_filter(filter_condition: TagFilterCondition):
        key_att = getattr(TagKey, filter_condition.key_field)
        tag_att = getattr(Tag, filter_condition.tag_field)
        operator = operator_from_str(filter_condition.operator)
        key_condition = key_att == filter_condition.key_value
        tag_condition = operator(tag_att, filter_condition.tag_value)
        return and_(key_condition, tag_condition)

    def _resolve_deep_identifier(self, deep_id:DeepIdentifier) -> str:
        if not deep_id.is_name_chain:
            return deep_id.uuid

        current_schema_id = self._collection_schema_id
        for name in deep_id.sub_schemas_name_chain:
            sub_schema = self._session.query(SubSchema).filter_by(parent_schema_id=current_schema_id, name=name).one_or_none()

            if sub_schema is None:
                raise ValueError(f"No sub schema named '{name}' found under schema ID {current_schema_id}")

            current_schema_id = sub_schema.child_schema_id

        field = self._session.query(Field.id).filter_by(
            schema_id=current_schema_id,
            name=deep_id.tail_field_name
        ).one_or_none()

        if field is None:
            raise ValueError(f"Field '{deep_id.tail_field_name}' not found in schema ID {current_schema_id}")

        return field.id


    def _build_data_filter(self, filter_condition: DataFilterCondition):
        field_id = self._resolve_deep_identifier(filter_condition.deep_identifier)
        operator = operator_from_str(filter_condition.operator)

        field_condition = ConstValue.field_id == field_id
        value_condition = operator(ConstValue.value, str(filter_condition.value.value))
        return and_(field_condition, value_condition)

    def execute_simple_filter_condition(self, filter_condition:SimpleFilterCondition, query:Query) -> Query:
        condition = self._build_simple_filter_condition(filter_condition)
        return query.filter(condition)

    @staticmethod
    def _generate_group_by_clause(filters:Filters, query:Query, select_class:type) -> Query:
        having_clauses = []

        if filters.tag_filters:
            having_clauses.append(func.count(Tag.id.distinct()) == len(filters.tag_filters))
        if filters.data_filters:
            having_clauses.append(func.count(ConstValue.id.distinct()) == len(filters.data_filters))

        return query.group_by(getattr(select_class, 'id')).having(and_(*having_clauses))

    def execute_filters(self, filters:Filters, select_class:type, query:Query) -> Query:

        if self._collection_schema_id:
            query = query.filter(Schema.id == self._collection_schema_id)

        for sf in filters.simple_filters:
            query = self.execute_simple_filter_condition(sf, query)

        tag_conditions = [self._build_tag_filter(tf) for tf in filters.tag_filters]
        data_conditions = [self._build_data_filter(tf) for tf in filters.data_filters]
        query = query.filter(or_(*tag_conditions))
        query = query.filter(or_(*data_conditions))

        query = self._generate_group_by_clause(filters, query, select_class)

        return query



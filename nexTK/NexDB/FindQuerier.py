from tarfile import data_filter
from uuid import UUID

from dacite import from_dict
from pydantic_core import from_json
from sqlalchemy.orm.collections import collection

from FilterQuerierHelper import FilterQuerierHelper
from collection_store import COLLECTION_STORE
from db.ImplicitJoiner import ImplicitJoiner
from db.models import Tag, TagKey, Schema, SubSchema, ConstValue, Field, Collection
from query_models.helper_query_models import Filters, SimpleFilterCondition
from query_models.reading_query_models import FindQuery
from sqlalchemy.orm import Session

from util import class_name_to_class


class FindQuerier:
    def __init__(self, Base:type):
        self._joiner = ImplicitJoiner(Base, exclude_clases=[SubSchema])
        self._filter_querier = FilterQuerierHelper()

    def _resolve_collection_data(self, query_model:FindQuery, session:Session) -> tuple[UUID, Filters]:
        if COLLECTION_STORE.exists(query_model.collection, session):
            filters = COLLECTION_STORE.get_filter(query_model.collection, session)
            schema_id = COLLECTION_STORE.get_schema_id(query_model.collection, session)
            return schema_id, filters

        collection_obj = session.query(Collection).filter_by(name=query_model.collection).one_or_none()
        if not collection_obj:
            raise ValueError(f"No collection named '{query_model.collection}' found")

        schema_id:UUID = collection_obj.schema_id
        filters_dict = from_json(collection_obj.filters)
        filters:Filters = from_dict(Filters, filters_dict)
        return schema_id, filters

    def _add_collection_filters(self, query_model:FindQuery, session:Session) -> Filters:
        if not query_model.collection:
            return query_model.filters

        schema_id, coll_filters = self._resolve_collection_data(query_model, session)
        self._filter_querier.set_collection_schema(schema_id)
        simple_filters = query_model.filters.simple_filters + coll_filters.simple_filters
        tag_filters = query_model.filters.tag_filters + coll_filters.tag_filters
        data_filters = query_model.filters.data_filters + coll_filters.data_filters
        return Filters(simple_filters, tag_filters, data_filters)

    def query(self, query_model:FindQuery, session:Session):
        self._filter_querier.set_session(session)
        self._joiner.reset()
        select_class = class_name_to_class(query_model.select_class)
        self._joiner.set_select_class(select_class)

        filters = self._add_collection_filters(query_model, session)

        for simple_filter in filters.simple_filters:
            filter_class = class_name_to_class(simple_filter.source_class)
            self._joiner.add_relation(filter_class)

        if len(filters.tag_filters) > 0:
            self._joiner.add_relation(Tag)
            self._joiner.add_relation(TagKey)

        if len(filters.data_filters) > 0:
            self._joiner.add_relation(Schema)
            self._joiner.add_relation(SubSchema)
            self._joiner.add_relation(Field)
            self._joiner.add_relation(ConstValue)

        query = session.query(select_class)
        query = self._joiner.build_joins(query)
        query = self._filter_querier.execute_filters(filters, select_class, query)

        return query.all()

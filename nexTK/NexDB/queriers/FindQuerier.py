
from dacite import from_dict
from pydantic_core import from_json

from FilterQuerierHelper import FilterQuerierHelper
from collection_store import COLLECTION_STORE
from db.ImplicitJoiner import ImplicitJoiner
from db.models import Tag, TagKey, Schema, SubSchema, ConstValue, Field, Collection
from queriers.AbstractQuerierClass import AbstractQuerier
from query_models.helper_query_models import Filters
from query_models.reading_query_models import FindQuery
from sqlalchemy.orm import Session

from util import class_name_to_class


class FindQuerier(AbstractQuerier):
    def __init__(self, Base:type):
        super().__init__()
        self._joiner = ImplicitJoiner(Base, exclude_clases=[SubSchema])
        self._filter_querier = FilterQuerierHelper()

    def set_session(self, session:Session):
        super().set_session(session)
        self._filter_querier.set_session(session)

    def _resolve_collection_data(self, query_model:FindQuery) -> tuple[str, Filters]:
        if COLLECTION_STORE.exists(query_model.collection, self._session):
            filters = COLLECTION_STORE.get_filter(query_model.collection, self._session)
            schema_id = COLLECTION_STORE.get_schema_id(query_model.collection, self._session)
            return schema_id, filters

        collection_obj = self._session.query(Collection).filter_by(name=query_model.collection).one_or_none()
        if not collection_obj:
            raise ValueError(f"No collection named '{query_model.collection}' found")

        schema_id:str = collection_obj.schema_id
        filters_dict = from_json(collection_obj.filters)
        filters:Filters = from_dict(Filters, filters_dict)
        return schema_id, filters

    def _add_collection_filters(self, query_model:FindQuery) -> Filters:
        if not query_model.collection:
            return query_model.filters

        schema_id, coll_filters = self._resolve_collection_data(query_model)
        self._filter_querier.set_collection_schema(schema_id)
        simple_filters = query_model.filters.simple_filters + coll_filters.simple_filters
        tag_filters = query_model.filters.tag_filters + coll_filters.tag_filters
        data_filters = query_model.filters.data_filters + coll_filters.data_filters
        return Filters(simple_filters, tag_filters, data_filters)

    def query_find(self, query_model:FindQuery):
        self._joiner.reset()
        select_class = class_name_to_class(query_model.select_class)
        self._joiner.set_select_class(select_class)

        filters = self._add_collection_filters(query_model)

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

        query = self._session.query(select_class)
        query = self._joiner.build_joins(query)
        query = self._filter_querier.execute_filters(filters, select_class, query)

        return query.all()

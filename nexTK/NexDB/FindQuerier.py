from FilterQuerierHelper import FilterQuerierHelper
from db.ImplicitJoiner import ImplicitJoiner
from db.models import Tag, TagKey, Schema, SubSchema, ConstValue, Field
from query_models.reading_query_models import FindQuery
from sqlalchemy.orm import Session

from util import class_name_to_class


class FindQuerier:
    def __init__(self, Base:type):
        self._joiner = ImplicitJoiner(Base, exclude_clases=[SubSchema])
        self._filter_querier = FilterQuerierHelper()

    def query(self, query_model:FindQuery, session:Session):
        self._filter_querier.set_session(session)
        self._joiner.reset()
        select_class = class_name_to_class(query_model.select_class)
        self._joiner.set_select_class(select_class)

        for simple_filter in query_model.filters.simple_filters:
            filter_class = class_name_to_class(simple_filter.source_class)
            self._joiner.add_relation(filter_class)

        if len(query_model.filters.tag_filters) > 0:
            self._joiner.add_relation(Tag)
            self._joiner.add_relation(TagKey)

        if len(query_model.filters.data_filters) > 0:
            self._joiner.add_relation(Schema)
            self._joiner.add_relation(SubSchema)
            self._joiner.add_relation(Field)
            self._joiner.add_relation(ConstValue)

        query = session.query(select_class)
        query = self._joiner.build_joins(query)
        query = self._filter_querier.execute_filters(query_model.filters, select_class, query)

        return query.all()

from sqlalchemy.orm import Session
from queriers.FilterQuerierHelper import FilterQuerierHelper
from query_models.reading_query_models import SearchQuery
from util import class_name_to_class


class SearchQuerier:

    def __init__(self):
        self._filter_querier = FilterQuerierHelper()
        self._session:Session|None = None

    def set_session(self, session:Session):
        self._session = session
        self._filter_querier.set_session(session)

    def query_search(self, query_model:SearchQuery):
        select_class = class_name_to_class(query_model.select_class)
        query = self._session.query(select_class)
        for sf in query_model.simple_filters:
            query = self._filter_querier.execute_simple_filter_condition(sf, query)

        return query.all()
from sqlalchemy.orm import Session

from queriers.helpers.AbstractQuerierClass import AbstractQuerier
from queriers.helpers.FilterQuerierHelper import FilterQuerierHelper
from query_models.reading_query_models import SearchQuery
from util import class_name_to_class

class SearchQuerier(AbstractQuerier):

    def __init__(self):
        super().__init__()
        self._filter_querier = FilterQuerierHelper()

    def set_session(self, session:Session):
        super().set_session(session)
        self._filter_querier.set_session(session)

    def query_search(self, query_model:SearchQuery):
        select_class = class_name_to_class(query_model.select_class)
        query = self._session.query(select_class)
        for sf in query_model.simple_filters:
            query = self._filter_querier.execute_simple_filter_condition(sf, query)

        return query.all()
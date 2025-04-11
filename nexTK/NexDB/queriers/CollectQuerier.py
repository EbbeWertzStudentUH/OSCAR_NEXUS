from collection_store import COLLECTION_STORE
from db.models import Schema
from queriers.helpers.AbstractQuerierClass import AbstractQuerier
from queriers.helpers.query_resolvers import simple_id_resolve
from query_models.reading_query_models import CollectQuery


class CollectQuerier(AbstractQuerier):

    def query_colect(self, query_model:CollectQuery):
        schema_id = simple_id_resolve(Schema, "schema", query_model.schema, self._session).id
        COLLECTION_STORE.save_collection(self._session, query_model.save_name, schema_id, query_model.filters)



from uuid import UUID

from sqlalchemy.orm import Session

from collection_store import COLLECTION_STORE
from db.models import Schema
from query_models.helper_query_models import SimpleId
from query_models.reading_query_models import CollectQuery


class CollectQuerier:

    @staticmethod
    def _resolve_schema_id(schema:SimpleId, session:Session) -> UUID:
        if schema.field == 'id':
            return schema.value

        schema_name = schema.value
        schema_obj = session.query(Schema.id).filter_by(name=schema_name).one_or_none()
        if schema_obj is None:
            raise ValueError(f"No Schema named '{schema_name}' found")
        return schema_obj.id

    def query(self, query_model:CollectQuery, session:Session):
        schema_id = self._resolve_schema_id(query_model.schema, session)
        COLLECTION_STORE.save_collection(session, query_model.save_name, schema_id, query_model.filters)



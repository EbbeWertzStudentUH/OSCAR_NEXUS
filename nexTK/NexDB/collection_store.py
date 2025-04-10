from uuid import UUID

from sqlalchemy.orm import Session

from query_models.helper_query_models import Filters

class CollectionStore:
    def __init__(self):
        self._collections:dict[tuple[str, Session], tuple[str, Filters]] = {}

    def exists(self, collection_name:str, session:Session)-> bool:
        return (collection_name, session) in self._collections

    def get_schema_id(self, collection_name:str, session:Session) -> str:
        return self._collections[(collection_name, session)][0]

    def get_filters(self, collection_name:str, session:Session) -> Filters:
        return self._collections[(collection_name, session)][1]

    def save_collection(self, session:Session, collection_name:str, schema_id:str, filters:Filters):
        self._collections[(collection_name, session)] = (schema_id, filters)

COLLECTION_STORE = CollectionStore()
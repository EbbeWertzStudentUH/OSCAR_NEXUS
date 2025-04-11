from pydantic_core import to_json

from Exceptions import EarlyQueryStopException
from collection_store import COLLECTION_STORE
from db.models import TagKey, Tag, Collection, Schema, Field, SubSchema
from queriers.helpers.AbstractQuerierClass import AbstractQuerier
from queriers.helpers.query_resolvers import simple_id_resolve
from query_models.helper_query_models import SimpleId
from query_models.mutating_query_models import TagTopicCreateQuery, TagCreateQuery, CollectionCreateQuery, \
    SchemaCreateQuery


class CreateQuerier(AbstractQuerier):

    def query_create_topic(self, query_model:TagTopicCreateQuery):
        tag_key = TagKey(name=query_model.name)
        self._session.add(tag_key)
        self._session.commit()

    def query_create_tag(self, query_model: TagCreateQuery):
        tag_key_id = simple_id_resolve(TagKey, "topic", query_model.key_id, self._session).id

        tag = Tag(name=query_model.name, tag_key_id=tag_key_id)
        self._session.add(tag)
        self._session.commit()

    def query_create_collection(self, query_model:CollectionCreateQuery):
        if not COLLECTION_STORE.exists(query_model.from_name, self._session):
            raise EarlyQueryStopException(f"No collection named '{query_model.from_name}' found in this query session")

        filters = COLLECTION_STORE.get_filters(query_model.from_name, self._session)
        schema_id = COLLECTION_STORE.get_schema(query_model.from_name, self._session)
        filters_json = to_json(filters).decode('utf-8')
        collection_obj = Collection(schema_id=schema_id, name=query_model.save_name, filters=filters_json)
        self._session.add(collection_obj)
        self._session.commit()

    def query_create_schema(self, query_model: SchemaCreateQuery):
        schema = Schema(name=query_model.name,info=query_model.info)
        self._session.add(schema)
        self._session.flush()  # to get schema.id for FK in fields/subschemas

        for f in query_model.fields:
            field = Field(schema_id=schema.id,name=f.name,datatype=f.data_type,is_constant=f.is_constant)
            self._session.add(field)

        for subs in query_model.sub_schemas:
            child_schema_id = simple_id_resolve(Schema, "schema", subs.schema_id, self._session).id
            sub_schema = SubSchema(
                parent_schema_id=schema.id,
                child_schema_id=child_schema_id,
                name=subs.name
            )
            self._session.add(sub_schema)

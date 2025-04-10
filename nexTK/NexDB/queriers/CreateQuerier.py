from query_models.mutating_query_models import TagTopicCreateQuery, TagCreateQuery, CollectionCreateQuery, \
    SchemaCreateQuery


class CreateQuerier:

    def query_create_topic(self, query_model:TagTopicCreateQuery):
        pass

    def query_create_tag(self, query_model:TagCreateQuery):
        pass

    def query_create_collection(self, query_model:CollectionCreateQuery):
        pass

    def query_create_schema(self, query_model:SchemaCreateQuery):
        pass
from operator import and_

from Exceptions import EarlyQueryStopException
from db.models import Tag, TagKey, Batch, TagAssignment
from queriers.helpers.AbstractQuerierClass import AbstractQuerier
from queriers.helpers.query_resolvers import simple_id_resolve
from query_models.helper_query_models import SimpleId
from query_models.mutating_query_models import TagAssignQuery


class TaggerQuerier(AbstractQuerier):

    def _resolve_tag_id(self, query_model:TagAssignQuery):
        tag_condition = getattr(Tag, query_model.tag_id.field) == query_model.tag_id.value
        key_condition = getattr(TagKey, query_model.topic_id.field) == query_model.topic_id.value
        tag_query = self._session.query(Tag.id).join(TagKey, Tag.tag_key_id == TagKey.id)
        tag_query = tag_query.filter(and_(tag_condition, key_condition))
        tag_obj = tag_query.one_or_none()
        if tag_obj is None:
            raise EarlyQueryStopException(f"No tag and/or topic was found for topic:'{query_model.topic_id.value}', tag:'{query_model.tag_id.value}'")
        return tag_obj.id

    def query_tag(self, query_model:TagAssignQuery):
        tag_id = self._resolve_tag_id(query_model)
        batch_id = simple_id_resolve(Batch, "batch", query_model.batch_id, self._session).id
        tag_assignment = TagAssignment(tag_id=tag_id, batch_id=batch_id)
        self._session.add(tag_assignment)
        self._session.commit()

    def query_untag(self):
        pass


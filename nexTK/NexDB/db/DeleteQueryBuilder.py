from uuid import UUID
from sqlalchemy.orm import Session



class DeleteQueryBuilder:
    def __init__(self):
        self._delete_class = None
        self._uuid = None
        self._id_field = 'id'
    def set_delete_class(self, clazz:type):
        self._delete_class = clazz
    def delete_by_uuid(self, uuid:UUID):
        self._uuid = uuid
    def build(self, session:Session):
        id_field = getattr(self._delete_class, self._id_field)
        item = session.query(self._delete_class).filter(id_field == self._uuid).first()
        session.delete(item)
        session.commit()
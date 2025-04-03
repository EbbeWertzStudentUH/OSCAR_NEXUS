from uuid import UUID
from sqlalchemy.orm import Session



class DeleteQueryBuilder:
    def __init__(self):
        self.reset()
        
    def set_delete_class(self, clazz:type):
        self._delete_class = clazz
        
    def add_delete_by_uuid(self, uuid:UUID):
        self._uuid = uuid
        
    def build_and_commit(self, session:Session):
        id_field = getattr(self._delete_class, self._id_field)
        query = session.query(self._delete_class).filter(id_field == self._uuid)
        session.delete(query.first())
        session.commit()
        
    def reset(self):
        self._delete_class = None
        self._uuid = None
        self._id_field = 'id'
    
    def is_set(self) -> bool:
        return self._delete_class is not None
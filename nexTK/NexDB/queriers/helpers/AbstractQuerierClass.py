from abc import ABC
from sqlalchemy.orm import Session


class AbstractQuerier(ABC):
    def __init__(self):
        self._session: Session | None = None

    def set_session(self, session:Session):
        self._session = session
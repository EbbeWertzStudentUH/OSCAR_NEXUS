from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from db.models import Base

class DatabaseConnection:
    def __init__(self, db_url:str, echo=False):
        engine = create_engine(db_url, echo=echo)
        self._SessionClass = sessionmaker(bind=engine)
        self._sessions = []
        Base.metadata.create_all(engine)

    def make_session(self) -> Session:
        new_session = self._SessionClass()
        self._sessions.append(new_session)
        return new_session

    def remove_session(self, session: Session):
        self._sessions.remove(session)
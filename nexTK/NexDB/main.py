from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from NexQLInterpreter import NexQlInterpreter
from db.models import Base


DATABASE_URL = "sqlite:///NexDB.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

interpreter = NexQlInterpreter(Base)

def init_db():
    Base.metadata.create_all(engine)
    
init_db()
interpreter.parse("FIND 16b53aaf-cd25-4c06-9c55-c79cc227a90c", session)
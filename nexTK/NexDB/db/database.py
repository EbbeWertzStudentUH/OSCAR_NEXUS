import operator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Batch, Dataset, Schema

DATABASE_URL = "sqlite:///NexDB.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()

query = session.query(Batch)

query = query.join(Schema, Schema.id == Batch.schema_id)
query = query.filter(operator.lt(Batch.created, 5)).filter(Schema.name == 'a')


query_str = str(query.statement.compile(compile_kwargs={"literal_binds": True})) #literal binds, renders in the literals (otheriwse fields are compared against 'name_1' instead of the actual given name value)
print(query_str)


def init_db():
    Base.metadata.create_all(engine)

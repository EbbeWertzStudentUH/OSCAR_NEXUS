import operator
from networkx import Graph
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Query, sessionmaker

from models import Base, Batch, ColValue, ConstValue, Dataset, Field, Schema, Tag
from ImplicitJoiner import ImplicitJoiner

DATABASE_URL = "sqlite:///NexDB.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()

def init_db():
    Base.metadata.create_all(engine)
    
joiner = ImplicitJoiner(Base)
joiner._debug_print_edges()

query = session.query(ColValue)
joiner.set_select_class(ColValue)

joiner.add_relation(ConstValue)
joiner.add_relation(Dataset)
joiner.add_relation(Field)
joiner.add_relation(Schema)
joiner.add_relation(Batch)

joiner._debug_print_joins()

query, aliasses = joiner.build_joins(query)

print(aliasses)



print(str(query))
# query_str = str(query.statement.compile(compile_kwargs={"literal_binds": True})) #literal binds, renders in the literals (otheriwse fields are compared against 'name_1' instead of the actual given name value)
# print(query_str)
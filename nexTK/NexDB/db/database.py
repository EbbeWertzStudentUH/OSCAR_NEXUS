import operator
from networkx import Graph
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Query, sessionmaker

from models import Base, Batch, Dataset, Field, Schema
from ImplicitJoiner import ImplicitJoiner

DATABASE_URL = "sqlite:///NexDB.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()

def init_db():
    Base.metadata.create_all(engine)
    
joiner = ImplicitJoiner(Base)

query = session.query(Batch)
joiner.set_select_class(Batch)
for node1, node2, data in joiner._dependency_graph.edges(data=True):
    print(f"Edge: {node1} <--> {node2}".ljust(40), end='')
    print(''.join([f"{at}: {val}".ljust(40) for at, val in data.items()]))
    
joins = []
joiner.add_relation(Dataset)
joiner.add_relation(Field)

for j in joins:
    print(''.join([f"{i}".ljust(30) for i in j]))
print(str(query))
# query_str = str(query.statement.compile(compile_kwargs={"literal_binds": True})) #literal binds, renders in the literals (otheriwse fields are compared against 'name_1' instead of the actual given name value)
# print(query_str)
import operator
from networkx import Graph
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import sessionmaker
from models import Base, Batch, Dataset, Field, Schema

DATABASE_URL = "sqlite:///NexDB.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()



# query = query.join(Schema, Schema.id == Batch.schema_id)
# query = query.filter(operator.lt(Batch.created, 5)).filter(Schema.name == 'a')





def init_db():
    Base.metadata.create_all(engine)
    
import networkx as nx
from sqlalchemy.orm import class_mapper, aliased

def build_dependency_graph(base) -> Graph:
    graph = nx.Graph()  # Make it an undirected graph

    for class_ in base.registry.mappers:
        clazz = class_.class_
        table: Table = clazz.__table__
        
        graph.add_node(table, clazz=clazz)

    # separate loop, because all nodes need to be present already, to get mapped classes
    for table in graph.nodes:
        for column in table.columns:
            for fk in column.foreign_keys:
                source_class = graph.nodes[column.table]['clazz']
                target_class = graph.nodes[fk.column.table]['clazz']
                source_field = getattr(source_class, column.name)
                target_field = getattr(target_class, fk.column.name)

                graph.add_edge(column.table, fk.column.table, source_field=source_field, target_field=target_field)

    return graph



query = session.query(Batch)
graph = build_dependency_graph(Base)
for node1, node2, data in graph.edges(data=True):
    print(f"Edge: {node1} <--> {node2}".ljust(40), end='')
    print(''.join([f"{at}: {val}".ljust(40) for at, val in data.items()]))

print(str(query))
# query_str = str(query.statement.compile(compile_kwargs={"literal_binds": True})) #literal binds, renders in the literals (otheriwse fields are compared against 'name_1' instead of the actual given name value)
# print(query_str)
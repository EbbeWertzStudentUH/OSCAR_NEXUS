import operator
from networkx import Graph
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import Query, sessionmaker
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

def build_dependency_graph(base: type) -> Graph:
    graph = nx.Graph()

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

def generate_joins(joins: list, find_class: type, join_class: type, graph: Graph):

    path = nx.shortest_path(graph, source=find_class.__table__, target=join_class.__table__)
    
    for i in range(len(path) - 1):
        source_table = path[i]
        target_table = path[i + 1]
        source_field = graph[source_table][target_table]["source_field"]
        target_field = graph[source_table][target_table]["target_field"]
        joins.append((join_class, source_field, target_field))

    return joins


query = session.query(Batch)
graph = build_dependency_graph(Base)
for node1, node2, data in graph.edges(data=True):
    print(f"Edge: {node1} <--> {node2}".ljust(40), end='')
    print(''.join([f"{at}: {val}".ljust(40) for at, val in data.items()]))
    
joins = []
generate_joins(joins, Batch, Dataset, graph)
generate_joins(joins, Batch, Field, graph)
for j in joins:
    print(''.join([f"{i}".ljust(30) for i in j]))
print(str(query))
# query_str = str(query.statement.compile(compile_kwargs={"literal_binds": True})) #literal binds, renders in the literals (otheriwse fields are compared against 'name_1' instead of the actual given name value)
# print(query_str)
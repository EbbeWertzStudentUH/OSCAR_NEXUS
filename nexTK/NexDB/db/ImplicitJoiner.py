import networkx as nx
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import Query, aliased


class ImplicitJoiner:
    def __init__(self, Base:type):
        self._joins = set() # no duplicate joins allowed
        self._dependency_graph = self._build_dependency_graph(Base)
        self._selectClass = None
        
    def _build_dependency_graph(self, Base:type) -> nx.Graph:
        graph = nx.Graph()

        for class_ in Base.registry.mappers:
            clazz = class_.class_
            table: Table = clazz.__table__

            graph.add_node(table, clazz=clazz)
            
        fk_map = {}

        # separate loop, because all nodes need to be present already, to get mapped classes
        for table in graph.nodes:
            for column in table.columns:
                for fk in column.foreign_keys:
                    source_class = graph.nodes[column.table]['clazz']
                    target_class = graph.nodes[fk.column.table]['clazz']
                    source_field = column.name # '{other_table}_id' field
                    target_field = fk.column.name # 'id' field 

                    if (source_class, target_class) in fk_map.keys():
                        field = fk_map[(source_class, target_class)]
                        raise ValueError(f"⚠️Implicit relations only work when there are no multiple foreign keys with the same table pair. Both {source_class} -> {field} and {source_class} -> {source_field} relate to {target_class}. If explicit relations should be supported, please edit this implicit joiner module.")
                    fk_map[(source_class, target_class)] = source_field
                    
                    graph.add_edge(column.table, fk.column.table, source_field=source_field, target_field=target_field)

        return graph
    
    def set_select_class(self, clazz:type):
        self._selectClass = clazz
        
    def add_relation(self, join_class:type):
        select_table, join_table = self._selectClass.__table__, join_class.__table__
        path = nx.shortest_path(self._dependency_graph, source=select_table, target=join_table)
        if len(path) == 1: path *= 2
        for i in range(len(path) - 1):
            target_table = path[i]
            source_table = path[i + 1]
            source_field = self._dependency_graph[source_table][target_table]["source_field"]
            target_field = self._dependency_graph[source_table][target_table]["target_field"]
            self._joins.add((source_table, target_table, source_field, target_field))
    
    def build_joins(self, query:Query) -> tuple[Query, dict]:
        aliasses = {}
        for (source_table, target_table, source_field, target_field) in self._joins:
            source_class = self._dependency_graph.nodes[source_table]["clazz"]
            target_class = self._dependency_graph.nodes[target_table]["clazz"]
            target_class_aliased = aliased(target_class)
            source_atrr = getattr(source_class, source_field) # '{other_table}_id' field
            target_attr = getattr(target_class_aliased, target_field) # 'id' field 
            aliasses[target_class] = target_class_aliased
            query = query.join(target_class_aliased, source_atrr == target_attr)
        return query, aliasses
    
    def _debug_print_edges(self):
        for node1, node2, data in self._dependency_graph.edges(data=True):
            print(f"Edge: {node1} <--> {node2}".ljust(40), end='')
            print(''.join([f"{at}: {val}".ljust(40) for at, val in data.items()]))
    def _debug_print_joins(self):
        for j in self._joins:
            print("Join: ", end='')
            print(''.join([f"{i}".ljust(30) for i in j]))
import networkx as nx
from sqlalchemy import Column
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import Query, aliased

from db.models import Schema


class ImplicitJoiner:
    def __init__(self, Base:type):
        self._joins = [] # cannot be Set() cuz insertion order needs to be preserved. Duplication is manually handled
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
                    source_col = column # '{other_table}_id' column
                    target_col = fk.column # 'id' column 

                    if (source_class, target_class) in fk_map.keys():
                        col = fk_map[(source_class, target_class)]
                        raise ValueError(f"⚠️Implicit relations only work when there are no multiple foreign keys with the same table pair. Both {source_class} -> {col} and {source_class} -> {source_col} relate to {target_class}. If explicit relations should be supported, please edit this implicit joiner module.")
                    fk_map[(source_class, target_class)] = source_col
                    
                    graph.add_edge(column.table, fk.column.table, source_col=source_col, target_col=target_col)

        return graph
    
    def set_select_class(self, clazz:type):
        self._selectClass = clazz
        
    def add_relation(self, join_class:type):
        select_table, join_table = self._selectClass.__table__, join_class.__table__
        path = nx.shortest_path(self._dependency_graph, source=select_table, target=join_table)
        if len(path) == 1: path *= 2 # self referencing relation
        for i in range(len(path) - 1):
            existing_table: Table = path[i]
            new_table: Table = path[i + 1]
            source_col: Column = self._dependency_graph[existing_table][new_table]["source_col"]
            target_col: Column = self._dependency_graph[existing_table][new_table]["target_col"]
            source_is_exist = existing_table.columns.contains_column(source_col)
            existing_col = source_col if source_is_exist else target_col
            new_col = target_col if source_is_exist else source_col
            
            join = (existing_table, new_table, existing_col, new_col)
            if join not in self._joins:
                self._joins.append(join)
    
    def build_joins(self, query:Query) -> tuple[Query, dict[type, type]]:
        aliasses = {}

        for (_, new_table, _, _) in self._joins:
            clazz = self._dependency_graph.nodes[new_table]["clazz"]
            aliasses[clazz] = aliased(clazz)
        
        for (existing_table, new_table, existing_col, new_col) in self._joins:
            
            existing_class = self._dependency_graph.nodes[existing_table]["clazz"]
            new_class = self._dependency_graph.nodes[new_table]["clazz"]
            
            existing_class_aliased = aliasses[existing_class] if existing_class is not self._selectClass else existing_class
            new_class_aliased = aliasses[new_class] # new class is always aliased
            
            existing_atrr = getattr(existing_class_aliased, existing_col.name)
            new_attr = getattr(new_class_aliased, new_col.name)
            
            query = query.join(new_class_aliased, existing_atrr == new_attr)
            
        return query, aliasses
    
    def _debug_print_edges(self):
        for node1, node2, data in self._dependency_graph.edges(data=True):
            print(f"Edge: {node1} <--> {node2}".ljust(40), end='')
            print(''.join([f"{at}: {val}".ljust(40) for at, val in data.items()]))
    def _debug_print_joins(self):
        for j in self._joins:
            print("Join: ", end='')
            print(''.join([f"{i}".ljust(30) for i in j]))
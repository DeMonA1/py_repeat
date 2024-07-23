from typing import TypeVar, Generic, List, Optional
from graphs.edge import Edge
import sys

sys.path.insert(0, '..')        # import for search folder and ro bfs

from search.generic_search import bfs, Node, node_to_path


V = TypeVar('V')        # type of graph vertex

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]
        
    @property
    def vertex_count(self) -> int:
        return len(self._vertices)          # vertex count
    
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))       # edge count
    
    # add vertex into a graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])              # add empty list for edges
        return self.vertex_count - 1        # return index for the added vertices
    
    
    def del_vertex_by_index(self, index: int) -> None:
        deleted_vertex = self._vertices.pop(index)
        self.del_all_edges_for_vertex(index)
        print(f"Vertex - {deleted_vertex} with index {index} successfully deleted")
    
    def del_vertex_by_vertex(self, vertex: V) -> None:
        index: int = self.index_of(vertex)
        self.del_vertex_by_index(index)
    
    
    # It's an undirected graph, so we always add vertices in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())
        
    # Add the edge, using indeces of vertices (convinient method)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)
        
    # Add edge, looking through indeces of vertices (convinient method)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)
        
        
    def del_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.del_edge_by_indices(u, v)
        
    def del_edge_by_indices(self, u: int, v: int) -> None:
        for i in self._edges[u]:
            if i.v == v:
                self._edges[u].remove(i)
                print(f'Edge successfully delete {i}')
                break
        for k in self._edges[v]:
            if k.v == u:
                self._edges[v].remove(k)
                print(f'Edge successfully delete {k}')
                return
        print('There is nothing to delete, incorrect vertex')
    
    def del_all_edges_for_vertex(self, index: int) -> None:
        self._edges.pop(index)
        for vertex in self._edges:
            edges_for_del = []
            for edge in vertex:
                if edge.v == index:
                    edges_for_del.append(edge)                 
                if edge.v > index:
                    edge.v -= 1
                if edge.u > index:
                    edge.u -= 1
            for i in edges_for_del:
                vertex.remove(i) 
                    
                    
    # vertex search by index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]
    
    # index of vertex search into graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex) 
    
    # search for vertices that a vertex with a given index is associated with
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))
    
    # search for index of vertex; return its neighbors (convinient method)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))
    
    # return all of edges connected to a vertex with a given index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]
    
    # search for index of vertex; returned its edges (convinient method)
    def edges_for_vertes(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # simpified nice graph output
    def __str__(self) -> str:
        desc: str = ''
        for i in range(self.vertex_count):
            desc += f'{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n'
        return desc
    
if __name__ == '__main__':
    # test if simple graph constraction
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles",
                                    "Riverside", "Phoenix", "Chicago", "Boston", "New York", 
                                    "Atlanta", "Miami", "Dallas", "Houston", "Detroit", 
                                    "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago") 
    city_graph.add_edge_by_vertices("Seattle", "San Francisco") 
    city_graph.add_edge_by_vertices("San Francisco", "Riverside") 
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles") 
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside") 
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix") 
    city_graph.add_edge_by_vertices("Riverside", "Phoenix") 
    city_graph.add_edge_by_vertices("Riverside", "Chicago") 
    city_graph.add_edge_by_vertices("Phoenix", "Dallas") 
    city_graph.add_edge_by_vertices("Phoenix", "Houston") 
    city_graph.add_edge_by_vertices("Dallas", "Chicago") 
    city_graph.add_edge_by_vertices("Dallas", "Atlanta") 
    city_graph.add_edge_by_vertices("Dallas", "Houston") 
    city_graph.add_edge_by_vertices("Houston", "Atlanta") 
    city_graph.add_edge_by_vertices("Houston", "Miami") 
    city_graph.add_edge_by_vertices("Atlanta", "Chicago") 
    city_graph.add_edge_by_vertices("Atlanta", "Washington") 
    city_graph.add_edge_by_vertices("Atlanta", "Miami") 
    city_graph.add_edge_by_vertices("Miami", "Washington") 
    city_graph.add_edge_by_vertices("Chicago", "Detroit") 
    city_graph.add_edge_by_vertices("Detroit", "Boston") 
    city_graph.add_edge_by_vertices("Detroit", "Washington") 
    city_graph.add_edge_by_vertices("Detroit", "New York") 
    city_graph.add_edge_by_vertices("Boston", "New York") 
    city_graph.add_edge_by_vertices("New York", "Philadelphia") 
    city_graph.add_edge_by_vertices('Seattle', 'Chicago')
    
    print(city_graph)
    print(city_graph._edges)
    city_graph.del_vertex_by_vertex('Atlanta')
    print(city_graph._edges)
    print(city_graph)
    bfs_result: Optional[Node[V]] = bfs('Boston', lambda x: x == 'Miami',
                                        city_graph.neighbors_for_vertex)
    

    if bfs_result is None:
        print('No solution found using breadth-first search!')
    else:
        path: List[V] = node_to_path(bfs_result)
        print('Path from Boston to Miami:')
        print(path)

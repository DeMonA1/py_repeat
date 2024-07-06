import heapq


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}
    
    def add_adj(self, vertex, weight=0):
        self.connections[vertex] = weight
        
    def get_connections(self):
        return self.connections.keys()
    
    def get_weight(self, vertex):
        return self.connections[vertex]
    
    
class Graph:
    def __init__(self):
        self.vertex_dict = {}
        
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex
        
    def get_vertex(self, key):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return None
    
    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_dict:
            self.add_vertex(f)
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)
        
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 1)
graph.add_edge('B', 'C', 10)
vertex_a = graph.get_vertex('A')
vertex_b = graph.get_vertex('B')



def dijkstra(graph, starting_vertex, target):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    path = []
    
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                path.append((current_vertex, '--', neighbor))
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    aim = target
    fin_str = ''
    
    for i, _, j in reversed(path):
        if j == aim:
            fin_str += j+' --> '
            aim = i
    print(fin_str+starting_vertex)
    return distances

graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'D': 5, 'C': 1},
    'C': {'D': 3, 'E': 1, 'G': 10},
    'D': {'E': 8},
    'E': {'G': 15},
    'G': {},
}
# dijkstra(graph, 'A',target='E')
print(dijkstra(graph,'A',target='E'))

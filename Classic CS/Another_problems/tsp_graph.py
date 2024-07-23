import sys
sys.path.insert(0, '..')

from graphs.edge import Edge
from graphs.weighted_graph import WeightedGraph
from graphs.weighted_edge import WeightedEdge

from typing import Dict, List, Iterable, Tuple
from itertools import permutations



city_graph: WeightedGraph[str] = WeightedGraph(["Rutland", "Burlington","White River Junction",
                                "Bennington", "Brattleboro"])
city_graph.add_edge_by_vertices("Rutland", "Burlington", 67) 
city_graph.add_edge_by_vertices("Rutland", "White River Junction", 46) 
city_graph.add_edge_by_vertices("Rutland", "Bennington", 55) 
city_graph.add_edge_by_vertices("Rutland", "Brattleboro", 75) 
city_graph.add_edge_by_vertices("Burlington", "White River Junction", 91) 
city_graph.add_edge_by_vertices("Burlington", "Bennington", 122) 
city_graph.add_edge_by_vertices("Burlington", "Brattleboro", 153) 
city_graph.add_edge_by_vertices("White River Junction", "Bennington", 98) 
city_graph.add_edge_by_vertices("White River Junction", "Brattleboro", 65) 
city_graph.add_edge_by_vertices("Bennington", "Brattleboro", 40) 
cities = city_graph._vertices
city_permutations: Iterable[Tuple[str, ...]] = permutations(cities)
tsp_paths: List[Tuple[str, ...]] = [c + (c[0],) for c in city_permutations]



if __name__ == '__main__':
    best_path: Tuple[str, ...]
    min_distance: int = 99999999999         # random big number
    for path in tsp_paths:
        distance: int = 0
        last: str = path[0]
        for next in path[1:]:
            for i in city_graph.edges_for_vertes(last):
                if i.v == city_graph.index_of(next):
                    distance += i.weight
            last = next
        if distance < min_distance:
            min_distance = distance
            best_path = path
    print(f'The shortest path is {best_path} in {min_distance} miles')
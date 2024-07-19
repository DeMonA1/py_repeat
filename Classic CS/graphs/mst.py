import sys
from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge

sys.path.insert(0, '..')

from search.generic_search import PriorityQueue 


V = TypeVar('V')            # variable type in a graph
WeightedPath = List[WeightedEdge]       # type alias for paths

def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])


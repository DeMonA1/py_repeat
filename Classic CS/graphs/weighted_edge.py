from __future__ import annotations
from dataclasses import dataclass
import sys
sys.path.insert(0, '..')
from graphs.edge import Edge


@dataclass
class WeightedEdge(Edge):
    weight: float
    
    def reversed(self) -> WeightedEdge:
        return WeightedEdge(self.v, self.u, self.weight)
    
    # like this we can arrang edges by weight and to find a edge with mimnimal weight
    def __lt__(self, other: WeightedEdge) -> bool:
        return self.weight < other.weight
    
    def __str__(self) -> str:
        return f'{self.u} {self.weight} > {self.v}'
    
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class DirectedEdge:
    u: int          # from
    v: int          # to
    
    def __str__(self) -> str:
        return f'{self.u} -> {self.v}'
    
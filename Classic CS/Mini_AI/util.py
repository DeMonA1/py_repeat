from typing import List
from math import exp

# the scalar product of two vectors
def dot_prodct(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))

# classic sigmoid activation function 
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)
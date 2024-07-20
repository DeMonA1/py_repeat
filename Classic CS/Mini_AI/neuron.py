from typing import List, Callable
from util import dot_product


class Neuron:
    def __init__(self, weights: List[float], learning_rate: float,
                 activation_function: Callable[[float], float], derivative_activation_function:
                     Callable[[float], float]) -> None:
        self.weights: List[float] = weights
        self.activation_function: Callable[[float], float] = activation_function
        self.derivative_activation_function: Callable[[float], float] = \
        derivative_activation_function
        self.learning_rate: float = 0.0
        self.output_cache: float = 0.0
        self.delta: float = 0.0
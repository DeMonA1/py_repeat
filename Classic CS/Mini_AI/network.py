from __future__ import annotations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid

T = TypeVar('T')        # type of output data in the interpritation if neural network


class Network:
    def __init__(self, layer_structure: List[int], learning_rate: float,
                 activation_function: Callable[[float], float] = sigmoid,
                 derivative_activation_function: Callable[[float], float] = 
                 derivative_sigmoid) -> None:
        if len(layer_structure) < 3:
            raise ValueError('Error: Should be at least 3 layers (1 input, 1 hidden, 1 output)')
        self.layers: List[Layer] = []
        # input layer
        input_layer: Layer = Layer(None, layer_structure[0], learning_rate, activation_function,
                                   derivative_activation_function)
        self.layers.append(input_layer)
        # hidden laers and output layer
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate,
                               activation_function, derivative_activation_function)
            self.layers.append(next_layer)
        
    # Puts the input data on the first layer, then ouputs them from the 
    # first layer and gives in the second layer as the input data,
    # from second one - to third and etc.
    def outputs(self, input: List[float]) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)
    
    # Determines the change of each neurons on a base of error of ouput data
    # with by comparing it with expected output
    def backpropagate(self, expected: List[float]) -> None:
        # calculating of delta for neurons of the outpur layer
        last_layer: int = len(self.layers) - 1
        self.layers[last_layer].calculate_deltas_for_ouput_layer(expected)
        # calculating of delta for hidden layers in reverse order
        for l in range(last_layer - 1, 0, -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])
            
    # The backpropagate() function itself doesn't change the weight
    # Function update_weights uses deltas calculated in backpropagate()
    # to really change weights
    def update_weights(self) -> None:
        for layer in self.layers[1:]:       # skip the input layer
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + \
                    (neuron.learning_rate * (layer.previous_layer.output_cache[w]) * neuron.delta)
    
    # train() function uses results of the execution of the outputs() function
    # for each input data, compare them with the expected results and transmits
    # received in backpropagate() and update_weigths()
    def train(self, inputs: List[List[float]], expected: List[List[float]]) -> None:
        for location, xs in enumerate(inputs):
            ys: List[float] = expected[location]
            outs: List[float] = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()
            
    # For parameterized results, which required of classification,
    # this function return right tries amount and the percentage 
    # ratio compared to the total amount
    def validate(self, inputs: List[List[float]], expecteds: List[T],
                    interpret_output: Callable[[List[float]], T]) -> Tuple[int, int, float]:
        correct: int = 0
        for input, expected in zip(inputs, expecteds):
            result: T = interpret_output(self.outputs(input))
            if result == expected:
                correct += 1
        percentage: float = correct / len(inputs)
        return correct, len(inputs), percentage
            
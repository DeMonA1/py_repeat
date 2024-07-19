from __future__ import annotations
from typing import Tuple, List
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import randrange, random
from copy import deepcopy


class BitStr(Chromosome):
    def __init__(self, x: int, y: int) -> None:
        self.x: bytes = x.to_bytes(8, 'big')
        self.y: bytes = y.to_bytes(8, 'big')
        
    def fitness(self) -> float:     #6x - x^2 + 4y - y^2
        return 6 * int.from_bytes(self.x, 'big') - int.from_bytes(self.x, 'big') * int.from_bytes(self.x, 'big') + 4 * int.from_bytes(self.y, 'big') - int.from_bytes(self.y, 'big') * int.from_bytes(self.y, 'big')
    
    @classmethod
    def random_instance(cls) -> BitStr:
        return BitStr(randrange(100), randrange(100))
    
    def crossover(self, other: BitStr) -> Tuple[BitStr, BitStr]:
        child1: BitStr = deepcopy(self)
        child2: BitStr = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2
    
    def mutate(self) -> None:
        if random() > 0.5:                  # mutation of x
            if random() > 0.5:    
                self.x = (int.from_bytes(self.x, 'big') + 1).to_bytes(8, 'big')
            else:
                self.x = (int.from_bytes(self.x, 'big') - 1).to_bytes(8, 'big')
        else:                               # otherwise - mutation of y
            if random() > 0.5:
                self.y = (int.from_bytes(self.y, 'big') + 1).to_bytes(8, 'big')
            else:
                self.y = (int.from_bytes(self.y, 'big') - 1).to_bytes(8, 'big')
                
    def __str__(self) -> str:
        return f"X: {int.from_bytes(self.x, 'big')} Y: {int.from_bytes(self.y, 'big')} Fitness: {self.fitness()}"
    
    
    
if __name__ == '__main__':
    initial_population: List[BitStr] = [BitStr.random_instance() 
                                                for _ in range(20)]
    ga: GeneticAlgorithm[BitStr] = GeneticAlgorithm(
        initial_population=initial_population, threshold=13.0, max_generations=100,
        mutation_chance=0.1, crossover_chance=0.7)
    result: BitStr = ga.run()
    print(result)
                                                                

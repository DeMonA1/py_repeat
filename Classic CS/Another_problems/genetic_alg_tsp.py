from __future__ import annotations
import sys
sys.path.insert(0, '..')

from typing import Tuple, List, Dict, Iterable
from genetic_alg.chromosome import Chromosome
from genetic_alg.genetic_algorithm import GeneticAlgorithm
from random import shuffle, sample
from copy import deepcopy
from itertools import permutations


CITIES: List[str] = ['Rutland', 'Burlington', 'White River Junction', 
                     'Bennington', 'Brattleboro', 'Blyah']

vt_distances: Dict[str, Dict[str, int]] = { 
    "Rutland": 
        {"Burlington": 67, 
        "White River Junction": 46, 
        "Bennington": 55, 
        "Brattleboro": 75,
        'Blyah': 190}, 
    "Burlington": 
        {"Rutland": 67, 
        "White River Junction": 91, 
        "Bennington": 122, 
        "Brattleboro": 153,
        'Blyah': 100}, 
    "White River Junction": 
        {"Rutland": 46, 
        "Burlington": 91, 
        "Bennington": 98, 
        "Brattleboro": 65,
        'Blyah': 90}, 
    "Bennington": 
        {"Rutland": 55, 
        "Burlington": 122, 
        "White River Junction": 98, 
        "Brattleboro": 40,
        'Blyah': 212}, 
    "Brattleboro": 
        {"Rutland": 75, 
        "Burlington": 153, 
        "White River Junction": 65, 
        "Bennington": 40,
        'Blyah': 331},
    'Blyah':
        {'Rutland': 190,
         'Burlington': 100,
         'White River Junction': 90,
         'Bennington': 212,
         'Brattleboro': 331}}


class TSP(Chromosome):
    def __init__(self, cities: List[str]) -> None:
        self.cities: List[str] = cities
            
    def fitness(self) -> float:
        distance = 0.0
        last: str = self.cities[0]
        for next in self.cities[1:]:
            distance += vt_distances[last][next]
            last = next
        return 1 / distance

    @classmethod
    def random_instance(cls) -> TSP:
        cities = CITIES
        shuffle(cities)
        cities = cities + [cities[0]]
        return TSP(cities)
    
    def crossover(self, other: TSP) -> Tuple[TSP, TSP]:
        child1: TSP = deepcopy(self)
        child2: TSP = deepcopy(other)
       # print(child1.cities,  child2.cities)
        if child1.cities != len(set(child2.cities)):
            return child1, child2
        child1.cities[child1.cities.index(child2.cities[0])] = child1.cities[0]
        child1.cities[0], child2.cities[0] = child2.cities[0], child1.cities[0]
        child1.cities[-1], child2.cities[-1] = child2.cities[-1], child1.cities[-1]
        return child1, child2
    
    def mutate(self) -> None:           # swap two cities
        idx1, idx2 = sample(range(1, len(self.cities) - 1), k=2)
        self.cities[idx1], self.cities[idx2] = self.cities[idx2], self.cities[idx1]        
    
    def __str__(self) -> str:
        distance = 0.0
        last: str = self.cities[0]
        for next in self.cities[1:]:
            print(last)
            print(distance)
            distance += vt_distances[last][next]
            last = next
        return f"Path - {self.cities}: {distance}"
    
if __name__ == '__main__':
    initial_population: List[TSP] = [TSP.random_instance() for _ in range(500)]
    ga: GeneticAlgorithm[TSP] = GeneticAlgorithm(initial_population=
                    initial_population, threshold= 0.1, max_generations=1000,
                    mutation_chance=0.2, crossover_chance=0.3, 
                    selection_type=GeneticAlgorithm.SelectionType.ROULETTE)
    result: TSP = ga.run()
    print(result)
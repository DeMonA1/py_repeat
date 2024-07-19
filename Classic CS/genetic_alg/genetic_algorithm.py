from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean
from chromosome import Chromosome

C = TypeVar('C', bound=Chromosome)          # type of chromosoms

class GeneticAlgorithm(Generic[C]):
    SelectionType = Enum('SelectionType', 'ROULETTE TOURNAMENT')
    
    def __init__(self, initial_population: List[C], threshold: float,
                max_generations: int = 100, mutation_chance: float = 0.01,
                crossover_chance: float = 0.7, selection_type: SelectionType =
                SelectionType.TOURNAMENT) -> None:
        self._population: List[C] = initial_population
        self._threshold: float = threshold
        self._max_generation: int = max_generations
        self._mutation_chance: float = mutation_chance
        self._crossover_chance: float = crossover_chance
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type
        self._fitness_key: Callable = type(self._population[0]).fitness
        
    # Use the roulette method with normal arrangment, to choose 2 parents
    # Note: doesn't work at negative fitness values
    def _pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weights=wheel, k=2))
    
    # Choose randomly num_participants and take 2 bests from them 
    def _pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))
    
    
    # decreasing probability model
    def _pick_tournament_prob(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._population, k=num_participants)
        winners: List[C] = sorted(4, participants, key=self._fitness_key)
        wheel = []
        parents = []
        for i in range(2):
            for winner in winners:
                p: int =  ((1 - 0.7) ^ winners.index(winner)) * 0.7
                wheel.append(p)
            parent = choices(winners, weights=wheel, k=1)
            parents.append(parent[0])
            winners.remove(parent)
            wheel.pop(0)
        return tuple(parents)
        

    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        # continue, while dont fill new generation with individuals
        while len(new_population) < len(self._population):
            # choice 2 parents
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents: Tuple[C, C] = self._pick_roulette([x.fitness() for x in 
                                                            self._population])
            else:
                parents = self._pick_tournament(len(self._population) // 2)
            # potential crossover of 2 parents
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        # if number is odd, then one is excess, so remove its
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population           # replace the link
    
    # each individ mutates with chance _mutation_chance    
    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()
                
    # Executing genetic algorithm for max_generations iterations
    # and the return of best from found individuals
    def run(self) -> C:
        print((self._population[0]).fitness)
        best: C = max(self._population, key=self._fitness_key)
        for generation in range(self._max_generation):
            # early exit, if the threshold is exceeded
            if best.fitness() >= self._threshold:
                return best
            print(f'Generation {generation} Best {best.fitness()} Avg \
                  {mean(map(self._fitness_key, self._population))}')
            self._reproduce_and_replace()
            self._mutate()
            highest: C = max(self._population, key=self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest          # found new best result
        return best                 # best found result from _max_generations
                
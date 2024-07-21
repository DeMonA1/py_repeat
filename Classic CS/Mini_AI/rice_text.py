import csv
from typing import List
from util import normalize_by_future_scaling
from network import Network
from random import shuffle


def rice_interpret_output(output: List[float]) -> int:
    if max(output) == output[0]:
        return 'Cammeo'
    elif max(output) == output[1]:
        return 'Osmancik'

if __name__ == "__main__":
    rice_parameters: List[List[float]] = []
    rice_classifications: List[List[float]] = []
    rice_species: List[int] = []
    with open('Rice_Cammeo_Osmancik.csv', mode='r') as rice_file:
        rices: List = list(csv.reader(rice_file))
        shuffle(rices)          # receive our data strings in random order
        for rice in rices:
            parameters: List[float] = [float(n) for n in rice[0:7]]
            rice_parameters.append(parameters)
            species: str = rice[7]
            if species == 'Cammeo':
                rice_classifications.append([1.0, 0.0])
            else:
                rice_classifications.append([0.0, 1.0])
            rice_species.append(species)
    normalize_by_future_scaling(rice_parameters)
    
    rice_network: Network = Network([7, 8, 2], 0.5)
    
    # learning on the first 150 samples of rice, repeat 10 times
    rice_trainers: List[List[float]] = rice_parameters[0:3700]
    rice_trainers_corrects: List[List[float]] = rice_classifications[0:3700]
    for _ in range(2000):
        rice_network.train(rice_trainers, rice_trainers_corrects)

    # test on the last 28 rice samples in the data set
    rice_testers: List[List[float]] = rice_parameters[3700:3810]
    rice_testers_correcst: List[int] = rice_species[3700:3810]
    rice_results = rice_network.validate(rice_testers, rice_testers_correcst, rice_interpret_output)
    print(f'{rice_results[0]} correct of {rice_results[1]} = {rice_results[2] * 100}%')
import csv
from typing import List
from random import shuffle


def parse_csv(file_name: str, spicies_position: int, spicies_list: List[str]):
    sample_parameters: List[List[float]] = []
    sample_classifications: List[List[float]] = []
    sample_species: List[int] = []
    with open(file_name, mode='r') as sample_file:
        samples: List = list(csv.reader(sample_file))
        shuffle(samples)          # receive our data strings in random order
        for sample in samples:
            if spicies_position == 0:
                index = 0
                p = [float(n) for n in sample[1:]]
            else:
                index = len(samples[0]) - 1
                p = [float(n) for n in sample[0:index]]  
            parameters: List[float] = p
            sample_parameters.append(parameters)
            try:
                species: int = int(sample[index])
            except:
                species: int = str(sample[index])
            if species == spicies_list[0]:
                sample_classifications.append([1.0, 0.0, 0.0])
            elif species == spicies_list[1]:
                sample_classifications.append([0.0, 1.0, 0.0])
            else:
                sample_classifications.append([0.0, 0.0, 1.0])
            sample_species.append(species)
    return sample_parameters, sample_classifications, sample_species
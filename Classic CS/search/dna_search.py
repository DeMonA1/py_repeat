from enum import IntEnum
from typing import Tuple, List
from timeit import timeit
from bisect import bisect_left

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]       # a alias of type for codons
Gene = List[Codon]                                      # a alias of type for gene


gene_str: str = "ACTCGATCGTCTGCTAGCTAGCGTTATATGCGATCTATCAGATTAAGAGCTATCGACTAT" 

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):           # don't go beyond the line!
            return gene
        # initialize codon from 3 nucleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]],
                        Nucleotide[s[i + 2]])
        gene.append(codon)          # add codon into gene
    return gene

my_gene: Gene = string_to_gene(gene_str)


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
        return False
    
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.T)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.G)
print(linear_contains(my_gene, acg))        # True
print(linear_contains(my_gene, gat))        # False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:              # while there is a spot for a search
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))         # True 
print(binary_contains(my_sorted_gene, gat))         # False


l1 = list(range(0, 10**6))
print(bisect_left(l1, 500000))
print('bisect time: ', timeit('bisect_left(l1, 500000)', globals=globals()))
print('binary time: ', timeit('binary_contains(l1, 500000)', globals=globals()))
print('linear time: ',timeit('linear_contains(l1, 999999)', globals=globals()))

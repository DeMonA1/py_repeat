from random import choice
from string import ascii_uppercase
from typing import Dict, List, NamedTuple, Optional
import random

from csp import CSP, Constraint

Grid = List[List[str]]          # entering an alias for grids

class GridLocation(NamedTuple):
    row: int
    column: int
    
def generate_grid(variables: int, columns: int) -> Grid:
    # initialize a grid with random letters
    return [['' for c in range(columns)] for r in range(variables)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print(''.join(row))

def randomly_fill(domains: Dict[int, List[int]], sparseness: float):
        for row in domains.keys():
                if random.uniform(0, 1.0) < sparseness:
                    domains[row] = [random.randint(0, 9)]

                    
class SudokuConstraint(Constraint[int, int]):
    def __init__(self, variables: List[int]) -> None:
        super().__init__(variables)
        self.variables: List[int] = variables
    
    def satisfied(self, assignment: Dict[int, int]) -> bool:                                                                        #for row in range(0, 9):#list_check = []#for i in range(1, 10):#list_check.append(assignment[i + 9 * row]) #return len(set(list_check)) == len(list_check)
        
        # row check                                                                                                                                     
        rows = []
        for i in range(0, 9):
            rows.append([value for key, value in assignment.items() if key in range(1 + 9*i, 10 + 9*i)])
        print(rows)                                                                                                                                    
        for row in rows:                                                                                                    #print('len(set(row))-------', len(set(row)), 'print(row)------------------------!', print(set(row)))
            if not len(set(row)) == len(row):
                return False
            #return True
        
        #column check
        columns = []
        for i in range(1, 10):
            columns.append([value for key, value in assignment.items() if key in range(i, 81 + 1, 9)])
        for column in columns:                                                                                                    #print('len(set(row))-------', len(set(row)), 'print(row)------------------------!', print(set(row)))
            if not len(set(column)) == len(column):
                return False
        
        # square check
        for square in range(0, 9):
            list_check = []
            list_check.append([value for key, value in assignment.items() if key in (1, 2, 3, 10, 11, 12, 19, 20, 21)])
            if not len(set(list_check)) == len(list_check):
                return False   
             
            for j in range(4, 7):
                list_check2.append(assignment[j + 9 * square])
                
            for k in range(7,10):
                list_check3.append(assignment[k + 9 * square])
                
            if square in [2, 5, 8]:
                if not len(set(list_check1)) == len(list_check1) or \
                    not len(set(list_check2)) == len(list_check2) or \
                        not len(set(list_check3)) == len(list_check3):
                            return False
            else:
                list_check1 = []
                list_check3 = []
                list_check2 = []
                
        return True





    
if __name__ == '__main__':
    grid: Grid = generate_grid(9,9)
    
    #display_grid(grid)
    #print(grid)
    variables = list(range(1,82))
    domains = {a: list(range(1, 10)) for a in variables}
    randomly_fill(domains, 0.1)
    #print(domains)
    for domain in domains:
        if len(domains[domain]) == 1:               # if not isinstance(domains[domain], list):
            print(domain, ' : ', domains[domain])
    csp: CSP[int, int] = CSP(variables, domains)
    csp.add_constraint(SudokuConstraint(variables))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    print(solution)
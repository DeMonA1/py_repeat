from random import choice
from string import ascii_uppercase
from typing import Dict, List, NamedTuple, Optional
import random
from pprint import pprint

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

def randomly_fill(domains: Dict[int, List[int]]):
            domains[2] = [6]
            domains[10] = [1]
            domains[6] = [7]
            domains[14] = [8]
            domains[22] = [69]
            domains[23] = [1]
            domains[18] = [4]
            domains[40] = [3]
            domains[44] = [2]
            domains[45] = [6]
            

                    
class SudokuConstraint(Constraint[int, int]):
    def __init__(self, variables: List[int]) -> None:
        super().__init__(variables)
        self.variables: List[int] = variables
    
    def satisfied(self, assignment: Dict[int, int]) -> bool:                                                                        #for row in range(0, 9#for i in range(1, 10):#assignment[i + 9 * row]) #return len(set(list_check)) == len(list_check)
        
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
        #1
        list_check = [value for key, value in assignment.items() if key in (1, 2, 3, 10, 11, 12, 19, 20, 21)]
        if not len(set(list_check)) == len(list_check):
            return False   
        #2 
        list_check = [value for key, value in assignment.items() if key in (4, 5, 6, 13, 14, 15, 22, 23, 24)]
        if not len(set(list_check)) == len(list_check):
            return False
        #3    
        list_check = [value for key, value in assignment.items() if key in (7, 8, 9, 16, 17, 18, 25, 26, 27)]
        if not len(set(list_check)) == len(list_check):
            return False
        #4    
        list_check = [value for key, value in assignment.items() if key in (28, 29, 30, 37, 38, 39, 46, 47, 48)]
        if not len(set(list_check)) == len(list_check):
            return False
        #5
        list_check = [value for key, value in assignment.items() if key in (31, 32, 33, 40, 41, 42, 49, 50, 51)]
        if not len(set(list_check)) == len(list_check):
            return False
        #6
        list_check = [value for key, value in assignment.items() if key in (34, 35, 36, 43, 44, 45, 52, 53, 54)]
        if not len(set(list_check)) == len(list_check):
            return False
        #7
        list_check = [value for key, value in assignment.items() if key in (55, 56, 57, 64, 65, 66, 73, 74, 75)]
        if not len(set(list_check)) == len(list_check):
            return False
        #8
        list_check = [value for key, value in assignment.items() if key in (58, 59, 60, 67, 68, 69, 76, 77, 78)]
        if not len(set(list_check)) == len(list_check):
            return False
        #9
        list_check = [value for key, value in assignment.items() if key in (61, 62, 63, 70, 71, 72, 79, 80, 81)]
        if not len(set(list_check)) == len(list_check):
            return False
              
        return True





    
if __name__ == '__main__':
    grid: Grid = generate_grid(9,9)
    
    #display_grid(grid)
    #print(grid)
    variables = list(range(1,82))
    domains = {a: list(range(1, 10)) for a in variables}
    randomly_fill(domains)
    #print(domains)
    for domain in domains:
        if len(domains[domain]) == 1:               # if not isinstance(domains[domain], list):
            print(domain, ' : ', domains[domain])
    csp: CSP[int, int] = CSP(variables, domains)
    csp.add_constraint(SudokuConstraint(variables))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    print(solution)
    
    grid = [[], [], [], [], [], [], [], [], []]
    for k in grid:
        for i in range(9):
            k.append(' {} ')

    solution = { 1: 2,  2: 6,  3: 3,  4: 4,  5: 5,  6: 7,  7: 1,  8: 8,  9: 9,
                10: 1, 11: 5, 12: 7, 13: 2, 14: 8, 15: 9, 16: 3, 17: 6, 18: 4, 
                19: 4, 20: 8, 21: 9, 22: 69, 23: 1, 24: 3, 25: 2, 26: 5, 27: 7, 
                28: 3, 29: 1, 30: 2, 31: 5, 32: 4, 33: 6, 34: 7, 35: 9, 36: 8, 
                37: 5, 38: 7, 39: 8, 40: 3, 41: 9, 42: 1, 43: 4, 44: 2, 45: 6, 
                46: 6, 47: 9, 48: 4, 49: 7, 50: 2, 51: 8, 52: 5, 53: 1, 54: 3, 
                55: 7, 56: 2, 57: 1, 58: 8, 59: 6, 60: 4, 61: 9, 62: 3, 63: 5, 
                64: 8, 65: 3, 66: 5, 67: 9, 68: 7, 69: 2, 70: 6, 71: 4, 72: 1, 
                73: 9, 74: 4, 75: 6, 76: 1, 77: 3, 78: 5, 79: 8, 80: 7, 81: 2}
    pprint(grid)
    
    def convert(grid):
        for item in grid:
            if isinstance(item, list):
                for subitem in convert(item):
                    yield subitem
            else:
                yield item
    result = list(convert(grid))

    result = ''.join(result)
    result = result.format(*list(solution.values()))
    for i in [10, 21, 32, 43, 54, 65, 76]:
        result.insert(i, '\n')
r = ' 2  6  3  4  5  7  1  8  9 \
      1  5  7  2  8  9  3  6  4  \
      4  8  9  69 1  3  2  5  7 \
      3  1  2  5  4  6  7  9  8  \
      5  7  8  3  9  1  4  2  6  \
      6  9  4  7  2  8  5  1  3  \
      7  2  1  8  6  4  9  3  5  \
      8  3  5  9  7  2  6  4  1  \
      9  4  6  1  3  5  8  7  2 '
pprint(result, width=30)


from random import choice
from string import ascii_uppercase
from typing import Dict, List, NamedTuple, Optional

from csp import CSP, Constraint

Grid = List[List[str]]          # entering an alias for grids

class GridLocation(NamedTuple):
    row: int
    column: int
    
def generate_grid(rows: int, columns: int) -> Grid:
    # initialize a grid with random letters
    return [['*' for c in range(columns)] for r in range(rows)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print(''.join(row))
        
def generate_domain(rectangle: List[int], grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    r_height: int = rectangle[0]
    r_width: int = rectangle[1]
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + r_height)
            rows: range = range(row, row + r_width)
            if col + r_height  <= height and row + r_width <= width:
                # from left to right
                domain.append([GridLocation(r, c) for c in columns for r in rows])
                #print('!!!!', domain)
            if r_height == r_width: continue
            columns1: range = range(col, col + r_width)
            rows1: range = range(row, row + r_height)
            if col + r_width  <= width and row + r_height <= height:
                # from top to bottom
                domain.append([GridLocation(r, c) for r in rows1 for c in columns1])
    print(domain)
    return domain                


class RectangleSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, rectangles: List[str]) -> None:
        super().__init__(rectangles)
        self.rectangles: List[List[int]] = rectangles
        
    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        # the presence dupplicates grid position means that there is a match
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations) # or len(all_locations) - len(set(all_locations)) == 2
    
if __name__ == '__main__':
    a = (4, 3)
    b = (4, 2)
    c = (2, 2)
    grid: Grid = generate_grid(9,9)
    rectangles: List[List[int]] = [a, b, c]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for rectangle in rectangles:
        locations[rectangle] = generate_domain(rectangle, grid)
    #print('locations ---', locations)
    csp: CSP[str, List[GridLocation]] = CSP(rectangles, locations)
    csp.add_constraint(RectangleSearchConstraint(rectangles))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print('No soluton found!')
    else:
        print(solution.values())
        for grid_locations in solution.values():
            for location in grid_locations:
                (row, col) = (location.row, location.column)
                print(row,col, end='\n')
                grid[row][col] = '-'
        display_grid(grid)
                            
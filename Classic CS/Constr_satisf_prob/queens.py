from csp import Constraint, CSP
from typing import Dict, List, Optional


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns
    
    def satisfied(self, assignment: Dict[int, int]) -> bool:
        # q1c = queen is on the 1 vertical, q1r = queen is on the 1 horizontal
        for q1c, q1r in assignment.items():
            # q2c = queen is on the 2 vertical
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]      # q2r = queen is in the 2 horizontal
                    if q1r == q2r:                  # is the same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):        # is the one diagonal?
                        return False
            return True         # there is not conflicts

if __name__ == '__main__':
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    #for a in csp.constraints.values():
       # print(a[0].variables)
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print('No solution found!')
    else:
        print(solution)
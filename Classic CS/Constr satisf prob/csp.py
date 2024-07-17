from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod


V = TypeVar('V')        # Variable type for a variable
D = TypeVar('D')        # Domain type for definition domain

# Base class for all restrictions
class Constraint(Generic[V, D], ABC):
    # Variables for which there is a restriction
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables
        
    # Must be redifined in subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...
        
'''
Constraint satisfied problem consist from variables V type,
which have range of values known as definition domain,
D type and restrictions, which define whether it is acceptable
a select a given definiton domain for given variables
'''    
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables             # variables which will be resctricted
        self.domains: Dict[V, List[D]] = domains        # every variables domain
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for varible in self.variables:
            self.constraints[varible] = []
            if varible not in self.domains:
                raise LookupError('Every variable should have a domain assigned to it.')
            
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Variblae in constraint not in CSP')
            else:
                self.constraints[variable].append(constraint)
    
    # We check whether the assignment of the value corresponds 
    # by checking all the constraints for this variable
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    
    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # the assignment is completed, if there is assignment for each varibles(base case)
        if len(assignment) == len(self.variables):
            return assignment
        
        # get all variables from CSP, bot not from assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        
        # get all possible values of definition domain for first variable without assignment
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if there are no contradictions, continue recursion
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # if result is not found, finishing returns
                if result is not None:
                    return result
        return None
    
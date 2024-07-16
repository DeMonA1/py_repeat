from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, \
                    Callable, Set, Deque, Dict, Any, Optional
from typing import Protocol
from heapq import heappush, heappop



T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar('C', bound='Comparable')

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __lt__(self: C, other: C) -> bool:
        ...
        
    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other
    
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other
    
    def __ge__(self: C, other: C) -> bool:
        return not self < other
    
def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:          # while there is a spot for a search
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False
    
#if __name__ == '__main__':
    print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5))     # True
    print(binary_contains(['a', 'd', 'e', 'f', 'z'], 'f'))  # True
    print(binary_contains(['john', 'mark', 'ronald', 'sarah'], 'sheila'))  # False
    

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    @property
    def empty(self) -> bool:
        return not self._container      # not equal True for a empty container
    
    def push(self, item: T) -> None:
        self._container.append(item)
        
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)
    
    
class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0,
                 heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic
        
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], 
        List[T]]) -> Optional[Node[T]]:
    count_dfs = 0
    # fronier - is what we need to check
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    # explored - is where we have already been
    explored: Set[T] = {initial}
    
    # continue, while we have what to look through
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # if we found what we are looking for - done
        if goal_test(current_state):
            return current_node, count_dfs
        # to check where we can go further and what we havent explored already
        for child in successors(current_state):
            count_dfs += 1
            if child in explored:           # skip states that have already been explored
                continue
            explored.add(child) 
            frontier.push(Node(child, current_node))
    return None, count_dfs                         # we have checked everything, didnt find the way to target point

def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    # go back from the end to begining
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()
    @property
    def empty(self) -> bool:
        return not self._container          # dont equal True for a empty container
    
    def push(self, item: T) -> None:
        self._container.append(item)
        
    def pop(self) -> T:
        return self._container.popleft()    # FIFO
    
    def __repr__(self) -> str:
        return repr(self._container)
    
def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], 
        List[T]]) -> Optional[Node[T]]:
    count_bfs = 0
    # fronier - is what we need to check
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    # explored - is where we have already been
    explored: Set[T] = {initial}
    
    # continue, while we have what to look through
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # if we found what we are looking for - done
        if goal_test(current_state):
            return current_node, count_bfs
        # looking for unexplored cells to go to
        for child in successors(current_state):
            print(child)
            count_bfs += 1
            if child in explored:           # skip states that have already been explored
                continue
            explored.add(child) 
            frontier.push(Node(child, current_node))
    return None, count_bfs                         # we have checked everything, didnt find the way to target point


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    @property
    def empty(self) -> bool:
        return not self._container          # not True for a empty container
    
    def push(self, item: T) -> None:
        heappush(self._container, item)     # push in queue by priority

    def pop(self) -> T:
        return heappop(self._container)     # pop by priority
    
    def __repr__(self) -> str:
        return repr(self._container)
    

def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], 
        List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    count_astar = 0
    # fronier - is what we need to check
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    # explored - is where we have already been
    explored: Dict[T, float] = {initial: 0.0}
    
    # continue, while we have what to look through
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # if we found what we are looking for - done
        if goal_test(current_state):
            return current_node, count_astar
        # looking for unexplored cells to go to
        for child in successors(current_state):
            count_astar += 1
            new_cost: float = current_node.cost + 1
            # 1 - for grid, for more difficult apps there should be a cost finction here
            
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None, count_astar         # we have checked everything, didnt find the way to target point

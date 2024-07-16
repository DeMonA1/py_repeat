from typing import Dict, Generator
from functools import lru_cache
from time import time



def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

# if __name__ == '__main__':
    print(fib1(5))
    
 
 
    
def fib2(n: int) -> int:
    if n < 2:               # base cond
        return n
    return fib2(n - 2) + fib2(n - 1)
    # recursion

# if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))
    



memo: Dict[int, int] = {0: 0, 1: 1} # base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) 
    return memo[n]

#if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))
    
    

@lru_cache(maxsize=None)
def fib4(n: int) -> int:        # == fib2()
    if n < 2:                   # base case
        return n
    return fib4(n - 2) + fib4(n - 1)       # recursion

# if __name__ == '__main__':
    print(fib4(5))
    print(fib4(110))
    


def fib5(n: int) -> int:
    if n == 0: return n     # spec case
    last: int = 0           # fib(0)
    next: int = 1           # fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

# if __name__ == "__main__":
    print(fib5(5))
    print(fib5(50))
    
    

def fib6(n: int) -> Generator[int, None, None]:
    yield 0         # base case
    if n > 0: yield 1
    last: int = 0           # fib(0)
    next: int = 1           # fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next          # main iteration stage


# if __name__ == '__main__':
    for i in fib6(50):
        print(i)

def fib7(n: int) -> int:
    if n < 2:
        raise ValueError('Incorrect value')
    list1 = [0, 1]
    print(0, '\n',1, '\n', end='')
    for i in range(1, n):
        b = list1[i] + list1[i - 1]
        list1.append(b)
        print(b)

def test(n):
    time1 = time()
    fib7(n)
    time2 = time()
    result = time2 - time1
    print(result)
    return result

if __name__ == '__main__':
    assert test(18)
    assert test(0)

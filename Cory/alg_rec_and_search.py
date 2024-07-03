import time
from bisect import bisect_left


start = time.time()
count = 0
for i in range(1, 6):
    print(i)
    count += 1
end = time.time()
print(end - start, count)



#recursion
def factiorial_1(n):
    the_product = 1
    while n>0:
        the_product *= n
        n = n - 1
    return the_product

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def row(n):
    print(n)
    if n == 1:
        return
    return row(n - 1)



# linear search
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
print(linear_search(a_list, 91))

#binary_search
def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

#bisect
def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

w_list = ['dawn', 'drill', 'fall', 'moon', 'pool', 'rise', 'sun']

def compare(w1, w2):
    """True if w1 > w2"""
    w1, w2 = list(w1), list(w2)
    index = 0
    for i in w1:
        if len(w2) == index:
            break
        if i > w2[index]:
            return True
        elif i < w2[index]:
            return False
        index += 1
    
    
def bsearch_word(w_list: list, target: str):
    first = 0
    last = len(w_list) - 1
    mid = 0
    while True:
        mid = (first + last) // 2
        if w_list[mid] == target:
            return True
        if w_list[last] == w_list[first]:
            return False
        else:
            if compare(w_list[mid], target):
                last = mid - 1
            else:
                first = mid + 1

bsearch_word(w_list, 'rise')
                
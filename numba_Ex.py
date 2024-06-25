import math
from timeit import timeit
from numba import jit


def hypot(a, b):
    return math.sqrt(a ** 2 + b ** 2)
timeit('hypot(5, 6)', globals=globals())
timeit('hypot(5, 6)', globals=globals())


@jit
def hypot_jit(a, b):
    return math.sqrt(a ** 2 + b ** 2)
timeit('hypot_jit(5, 6)', globals=globals())
timeit('hypot_jit(5, 6)', globals=globals())


@jit(nopython=True)
def hypot_jit_nopy(a, b):
    return math.sqrt(a ** 2 + b ** 2)
timeit('hypot_jit_nopy(5, 6)', globals=globals())
timeit('hypot_jit_nopy(5, 6)', globals=globals())
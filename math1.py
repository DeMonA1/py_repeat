import numpy as np
from numpy import *


b = np.array([2, 4, 6, 8])
b.ndim
b.size
b.shape

a = np.arange(10)
a.ndim
a.shape
a.size

a = np.arange(7, 11)

a = np.arange(7, 11, 2)

f = np.arange(2.0, 9.8, 0.3)

g = np.arange(10, 4, -1.5, dtype=np.float64)



a = np.zeros((3,))
a.ndim
a.shape
a.size

b = np.zeros((2, 4))
b.ndim
b.shape
b.size

k = np.ones((3, 5))

m = np.random.random((3, 5))



a = np.arange(10)
a = a.reshape(2, 5)
a.ndim
a.shape
a.size

a = a.reshape(5, 2)
a.ndim
a.shape
a.size

a.shape = (2, 5)



a = np.arange(10)
a[7], a[-1]

a.shape = (2, 5)
a[1,2]

a = a.reshape(2, 5)
a[0, 2:]
a[-1, :3]
a[:, 2:4] = 1000



a = arange(4)
a *= 3

plain_list = list(range(4))
plain_list = [num * 3 for num in plain_list]

a = zeros((2,5)) + 17.0



# 4x + 5y = 20
#  x + 2y = 13
coefficients = np.array([ [4, 5], [1, 2] ])
dependents = np.array( [20, 13] )
answers = np.linalg.solve(coefficients, dependents)
product = np.dot(coefficients, answers)
np.allclose(product, dependents)

import csv, pandas

with open('../data_folder/books.csv', 'rt') as book:
    read = csv.DictReader(book)
    books = [r for r in read]
    print(books)
    pandas.read_csv(book)
    pandas.read_csv(book, sep='|')
    print(book)
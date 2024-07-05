import string
import math


def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False



s1 = 'Emperor Octavian'
s2 = 'Captain over Rome'
print(is_anagram(s1, s2))



def is_palindrom(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return False



s = 'Buy 1 get 2 free'
n1 = [c for c in s if c.isdigit()][-1]
print(n1)



def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt


new_list =  ["selftaught", "code", "sit", "eat", "programming", "dinner",
            "one", "two", "coding","a", "tech"]
c = [i for i in new_list if len(i) > 4]


def is_even(num):
    return not num & 1


def is_power(n):
    if n & (n - 1) == 0:
        return True
    return False


def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
            

# greatest common divisor
"""def gcf(i1, i2):
    gcf = None
    if i1 < 0 or i2 < 0:
        raise ValueError('Numbers must be positive.')
    
    if i1 == 0:
        return i2
    if i2 == 0:
        return i1
    
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
    
    for i in range(1, smaller + 1):
        if i1 % i == 0 and i2 % i == 0:
            gcf = i
    return gcf

gcf(20, 12)"""


# Euclidean algorithm
def gcf(x, y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    return [i for i in range(2, n) if is_prime(i)]


# sieve of Eratosthenes
def sieve(n):
    n1 = range(0, n+1)
    a = [True for i in n1]
    for i in range(2, n+1):
        if i**2 <= n and a[i] == True:
            for j in range(0, n+1):
                j = i**2 + j*i
                if j <= n:
                    a[j] = False

    return [i for i in range(2,len(a)) if a[i]]
sieve(200)
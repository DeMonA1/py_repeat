def prime_factors(h):
    upperbound = int(input('Upper bound?'))
    max_prime_factors = 0
    for counter in range(upperbound):
        factors = prime_factors(counter)
        if factors > max_prime_factors:
            max_prime_factors = factors
prime_factors(1)
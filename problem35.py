"""
Circular primes
The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from itertools import product
from digits import undigits
from primes import eratos_lt
from comb_it import cyclic_permutations

is_prime = eratos_lt(10**6)
n_circular_primes = len([2, 3, 5, 7]) # treat one-digit primes separately

# Any prime with two or more digits will end on one of these digits, and
# thus any circular prime most consist entirely of these digits
possible_digits = [1,3,7,9]
for n_digs in range(2, 7):
    for digs in product(possible_digits, repeat=n_digs):
        if all(is_prime[undigits(d)] for d in cyclic_permutations(digs)):
            n_circular_primes += 1

print(n_circular_primes)
correct_answer = "55"
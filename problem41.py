"""
Pandigital prime
We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once. For example, 2143 is a 4-digit 
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations

from digits import undigits
from primes import is_prime


# It is easy to see (by considering the sum of the digits) that all 
# pandigital numbers with 8 or 9 digits are multiples of 3, so the 
# largest pandigital prime can at most have 7 digits

for digs in permutations(range(7, 0, -1)):
    n = undigits(digs)
    if is_prime(n):
        result = n
        break
else:
    raise Exception("No result found :(")

print(result)
correct_answer = "7652413"
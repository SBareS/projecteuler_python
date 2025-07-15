"""
At Least Four Distinct Prime Factors Less Than 100

It can be verified that there are 23 positive integers less than 1000 that are
divisible by at least four distinct primes less than 100.

Find how many positive integers less than 10^16 are divisible by at least four
distinct primes less than 100.
"""

# Routine application of Mobius-inversion/generalized PIE.

from itertools import combinations
from math import comb, prod
from primes import primes_lt


upper_bound = 10**16 - 1
primes = primes_lt(100)
acc = 1
for i, p in enumerate(primes):
    acc *= p
    if acc > upper_bound:
        max_primes = i
        break

result = 0
for n in range(4, max_primes + 1):
    result += (-1)**n * comb(n-1, 3) * sum(upper_bound//prod(ps) for ps in combinations(primes, n))
print(result)

correct_answer = "785478606870985"
"""
Prime summations
It is possible to write ten as the sum of primes in exactly five
different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in
over five thousand different ways?
"""

from functools import cache
from itertools import count

from primes import primes_lt


primes = primes_lt(1000)  # guesstimate
@cache
def n_prime_partitions(n, min_prime_ind):
    if n == 0:
        return 1
    if n == 1:
        return 0
    result = 0
    for i in count(min_prime_ind):
        p = primes[i]
        if p > n:
            return result
        result += n_prime_partitions(n-p, i)

for n in count():
    if n_prime_partitions(n, 0) > 5000:
        result = n
        break

print(result)
correct_answer = "71"
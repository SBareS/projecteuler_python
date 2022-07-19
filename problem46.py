"""
Goldbach's other conjecture
It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

9 = 7 + 2*12
15 = 7 + 2*22
21 = 3 + 2*32
25 = 7 + 2*32
27 = 19 + 2*22
33 = 31 + 2*12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?
"""

from itertools import count, takewhile
from math import isqrt

from primes import primes_seq
from sequences import CachedSequence

primes = CachedSequence(primes_seq())

def is_twice_square(n):
    q, r = divmod(n, 2)
    return r == 0 and isqrt(q)**2 == q

for n in count(3, 2):
    if any (is_twice_square(n - p) for p in takewhile(lambda x: x <= n, primes)):
        continue
    result = n
    break

print(result)
correct_answer = "5777"
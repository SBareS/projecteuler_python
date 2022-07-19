"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


import math

from primes import primes_lt

N = 600851475143
prime_bound = math.isqrt(N+1)

for p in primes_lt(prime_bound):
    while N % p == 0 and N != p:
        N //= p
    if p == N:
        break
else:
    raise Exception("Something went wrong")

print(N)
correct_answer = "6857"
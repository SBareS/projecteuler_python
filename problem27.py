"""
Quadratic primes
Euler discovered the remarkable quadratic formula:
$$n^2 + n + 41$$
It turns out that the formula will produce 40 primes for the consecutive
integer values 0 <= n <= 39. However, when n = 40, 
$40^2 + 40 + 41 = 40(40+1) + 41$ is divisible by 41, and certainly when
n = 41, $41^2 + 41 + 41$ is clearly divisible by 41.

The incredible formula $n^2 - 79n + 1601$ was discovered, which produces
80 primes for the consecutive values 0 <= n <= 79. The product of the 
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
$$n^2 + an + b,$$
where |a| < 1000 and |b| <= 1000
where |n| is the modulus/absolute value of n, e.g. and |11| = 11 and 
|-4| = 4
Find the product of the coefficients, a and b, for the quadratic 
expression that produces the maximum number of primes for consecutive 
values of n, starting with n = 0.
"""

from functools import partial
from itertools import count, takewhile

from primes import eratos_lt

is_prime = eratos_lt(1000**2 + 1000 + 1000)
small_primes = [p for p in range(1000) if is_prime[p]]

def is_pos_and_prime(n):
    return n > 0 and is_prime[n]

def quadr_poly(a, b, x):
    return x**2 + a*x + b

most_primes = 0
result = None
for a in range(-999, 1000):
    for b in small_primes:  # f(0)=b must be prime
        f = partial(quadr_poly, a, b)
        n_primes = len(list(takewhile(is_pos_and_prime, map(f, count()))))
        if n_primes > most_primes:
            most_primes = n_primes
            result = a*b

print(result)
correct_answer = "-59231"
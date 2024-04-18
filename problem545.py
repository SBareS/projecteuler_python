"""
Faulhaber's Formulas
The sum of the kth powers of the first n positive integers can be expressed as
a polynomial of degree k+1 with rational coefficients, the Faulhaber's 
Formulas: 1^k + 2^k + ... + n^k = a1*n + a2*n^2 + ... + ak n^k + a(k+1)n^(k+1),
where ai's are rational coefficients that can be written as reduced fractions
pi/qi (if ai = 0, we shall consider qi=1).

For example, 1^4 + 2^4 + ... + n^4 = -1/30 n + 1/3 n^3 + 1/2 n^4 + 1/5 n^5.
Define D(k) as the value of q1 for the sum of kth powers (i.e. the denominator
of the reduced fraction a1).
Define as F(m) the mth value of k >= 1 for which D(k) = 20010.
You are given D(4) = 30 (since a1 = -1/30), D(308) = 20010, F(1) = 308, F(10) = 96404.

Find F(10^5)
"""

from itertools import count
from math import lcm
import factorization
from factorization import divisors
from primes import is_prime

# This is just a roundabout way of asking us to find Bernoulli numbers with 
# denominator 20010. Von Staudt–Clausen theorem to the rescue.

N = 10**5

# Generate way more primes+hints than we need, as this 
# saves us time on prime-testing in the long run
prime_bound = 10**7
factorization.generate_default_primes_and_hints(prime_bound)

#20010 = 2*3*5*23*29
good_primes = [2, 3, 5, 23, 29]
n0 = lcm(*(p-1 for p in good_primes))

n_found = 0
# Loop over 308*k. We can skip even k, 
# since those give 88+1 = 89 in the denominator
for n in count(n0, 2*n0):
    # By similar arguments, we can skip multiples of a few other small primes
    if any(n0 % d == 0 for d in [3, 5, 23]):
        continue
    # In the remaining cases, we have to check every divisor :-()
    if any(d+1 not in good_primes and is_prime(d+1) for d in divisors(n)):
        continue

    n_found += 1
    if n_found == N:
        result = n
        break

print(result)
correct_answer = "921107572"
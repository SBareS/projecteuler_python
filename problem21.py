"""
Amicable numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less 
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable 
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import factorization
from arithfunct import sigma_nat

N = 10_000
# It can be shown that d(n) <= 7.1*n, so 8*N primes should be more than enough
factorization.generate_default_hints(8*N)

def d(n):
    return sigma_nat(n) - n
def is_amicable(n):
    dn = d(n)
    return dn != n and d(dn) == n

amicable_numbers = [n for n in range(2, N) if is_amicable(n)]

print(sum(amicable_numbers))
correct_answer = "31626"
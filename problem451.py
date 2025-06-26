"""
Modular Inverses

Consider the number 15.
There are eight positive numbers less than 15 which are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14.
The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14
because
1*1 mod 15 = 1
2*8 mod 15 = 1
4*4 mod 15 = 1
7*13 mod 15 = 1
11*11 mod 15 = 1
14*14 mod 15 = 1
Let I(n) be the largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself.
So I(15) = 11.
Also and I(100) = 51 and I(7) = 1.

Find the sum of I(n) for 3 <= n <= 2 * 10^7.
"""

from itertools import product
import factorization
from factorization import prime_power_factors
from mod_arith import orth_idemp

upper_bound = 2 * 10**7
factorization.generate_default_primes_and_hints(upper_bound + 1)

def mod_selfinv_pp(q):
    if q % 2 == 0:
        if q == 2:
            return [1]
        elif q == 4:
            return [1, 3]
        else:
            return [1, q//2 - 1, q//2 + 1, q - 1]
    return [1, q - 1]

result = 0
for n in range(3, upper_bound + 1):
    #if n % 100_000 == 0:
    #    print(n)
    biggest = 1
    pp = [p**k for p, k in prime_power_factors(n)]
    es = orth_idemp(pp)
    for xs in product(*map(mod_selfinv_pp, pp)):
        t = sum(e * x for e, x in zip(es, xs)) % n
        if biggest < t < n - 1:
            biggest = t
    result += biggest
print(result)

correct_answer = "153651073760956"
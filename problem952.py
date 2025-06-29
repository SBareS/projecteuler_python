"""
Order Modulo Factorial

Given a prime p and a positive integer n < p, let R(p, n) be the 
multiplicative order of p modulo n!. In other words, R(p, n) is the minimal 
positive integer r such that

$$p^r \equiv 1 \pmod{n!}$$

For example, R(7, 4) = 2 and R(10^9 + 7, 12) = 17280.

Find R(10^9 + 7, 10^7). Give your answer modulo 10^9 + 7.
"""

from collections import defaultdict

from digits import digits
import factorization
from mod_arith import order_modppow_pp
from primes import is_prime


p = the_mod = 10**9 + 7
n = 10**7

factorization.generate_default_primes_and_hints(n)
primes = [q for q in range(n+1) if is_prime(q)]

result_pp = defaultdict(int)
for q in primes:
    nuq = (n - sum(digits(n, q)))//(q - 1)
    for qq, kk in order_modppow_pp(p, q, nuq):
        result_pp[qq] = max(result_pp[qq], kk)

result = 1
for q, k in result_pp.items():
    result = result * pow(q, k, the_mod) % the_mod
print(result)

correct_answer = "794394453"
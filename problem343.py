"""
Fractional Sequences
For any positive integer k, a finite sequence ai of fractions xi/yi is 
defined by:
a1 = 1/k
and
ai = (x(i-1) + 1)/(y(i-1) - 1) reduced to lowest terms for i > 1.
When ai reaches some integer n, the sequence stops. (That is, when yi = 1.)
Define f(k) = n.
For example, for k = 20:
1/20 -> 2/19 -> 3/18 = 1/6 -> 2/5 -> 3/4 -> 4/3 -> 5/2 -> 6/1 = 6
So f(20) = 6.
Also f(1) = 1, f(2) = 2, f(3) = 1 and the sum of f(k**3) 
for 1 <= k <= 100 equals 118937. Find the sum of f(k**3)
for 1 <= k <= 2 * 10**6. 
"""

# f(k) = (largest prime factor of k) - 1
# All we need then is to find the largest prime factors of
# k**3 + 1 = (k + 1)*(k**2 - k + 1)
# For both factors, we can divide out all but the largest prime with a sieve.
# For the second factor this means we need to solve a quadratic modulo p.

from math import isqrt

from mod_arith import sqrt_modp
from primes import primes_lt

kbound = 2 * 10**6

primes = primes_lt(isqrt(kbound**2 - kbound + 1) + 1)

# Compute largest prime factors of k+1 ...
lpf1 = [k + 1 for k in range(kbound+1)]
for p in primes:
    if p*p > kbound + 1:
        break
    for k in range(p*p - 1, kbound+1, p):
        while lpf1[k] > p and lpf1[k] % p == 0:
            lpf1[k] //= p

# ... and of k**2 - k + 1
lpf2 = [k**2 - k + 1 for k in range (kbound+1)]
for p in primes:
    if p % 3 == 2:
        continue # No roots of x**2 - x + 1 modulo p

    for d in sqrt_modp(-3, p):
        c = (1 + d)*(p+1)//2 % p # root of x**2 - x + 1 modulo p
        for k in range(c, kbound+1, p):
            while lpf2[k] > p and lpf2[k] % p == 0:
                lpf2[k] //= p

lpf = [max(lpf1[k], lpf2[k]) for k in range(kbound + 1)]

# print(lpf1)
# print(lpf2)
# print(lpf)
print(sum(lpf) - kbound - 1)
correct_answer = "269533451410884183"
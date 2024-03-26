"""
Pisano Periods 1

For every positive integer n the Fibonacci sequence modulo n is periodic. The
period depends on the value of n. This period is called the Pisano period for 
n, often shortened to pi(n).

There are three values of n for which pi(n) equals 18: 19, 38 and 76. The sum
of those smaller than 50 is 57.

Find the sum of the values of n smaller than 1 000 000 000 for which pi(n) 
equals 120. 
"""

from math import gcd, isqrt
from arithfunct import sigma_nat
import factorization
from matrix import Mat22

factorization.generate_default_primes(isqrt(10**9) + 1)
divisor_bound = 10 ** 9

M22 = Mat22(int)

#Sum of divisors less than N. This implementation is terribly slow, unless n 
#is only a bit smaller than N
def sigma_bounded(n, N):
    s = sigma_nat(n)
    i = 1
    while n // i >= N:
        if n % i == 0:
            s -= n // i
        i = i + 1
    return s

fibmat = M22(1, 1, 1, 0)
idmat = M22.identity

def F(n):
    return sigma_bounded(gcd(*fibmat ** n - idmat), divisor_bound)

# inclusion-exclusion
print(F(120) - F(120//2) - F(120//3) - F(120//5) 
      + F(120//6) + F(120//10) + F(120//15) 
      - F(120//30))
correct_answer = "44511058204"
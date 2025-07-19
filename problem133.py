"""
Repunit Nonfactors

A number consisting entirely of ones is called a repunit. We shall define 
R(k) to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10^n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is 
divisible by 17. Yet there is no value of n for which R(10^n) will divide by 
19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes
below one-hundred that can be a factor of R(10^n).

Find the sum of all the primes below one-hundred thousand that will never be a
factor of R(10^n).
"""

# p divides some R(10**n) = (10**10**n - 1)//9 iff 10**10**n is 1 mod p for 
# some n, which happens iff 10**n eventually becomes a multiple of the order
# of 10 mod p, i.e. iff the only prime divisors of the order of 10 mod p are 
# 2 and 5. We are looking for primes where this doesn't happen, i.e. where the
# order of 10 has some prime factor other than 2 and 5.

import factorization
from mod_arith import order_modp
from primes import is_prime

upper_bound = 100_000
factorization.generate_default_hints(upper_bound)
primes = [p for p in range(upper_bound) if is_prime(p)]

result = 0
for p in primes:
    if p <= 5:
        #2, 3, 5 are bad primes for this problem, handle separately (we want p
        # coprime to 10 and to 9), so handle separately.
        result += p
        continue
    
    k = order_modp(10, p)
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    if k != 1:
        result += p

print(result)

correct_answer = "453647705"
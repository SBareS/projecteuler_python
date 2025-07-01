"""
Divisors of Binomial Product

Let $B(n) = \\prod_{k=0}^n \\binom{n}{k}$, a product of binomial coefficients.
For example, B(5) = 1 * 5 * 10 * 10 * 5 * 1 = 2500.

Let $D(n) = \\sum_{d|B(n)}d$, the sum of the divisors of B(n).

For example, the divisors of B(5) are 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 
250, 500, 625, 1250 and 2500, so D(5) = 1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 
+ 100 + 125 + 250 + 500 + 625 + 1250 + 2500 = 5467.

Let $S(n) = \\Sum_{k=1}^n D(k)$.
You are given S(5)=5736, S(5) = 141740594713218418 and 
S(10) mod 1000000007 = 332792866.

Find S(20000) mod 1000000007. 
"""

from itertools import accumulate

from mod_arith import inverse_table
from primes import primes_lt

the_mod = 1_000_000_007
N = 20_000

primes = primes_lt(N+1)
inv_tab = inverse_table(the_mod, primes[-1]-1)

def nup(n, p):
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result

fac_nup = [list(accumulate((nup(n, p) for n in range(1, N+1)), initial=0)) for p in primes]
fac_nup_sum = [list(accumulate(lst)) for lst in fac_nup]

def D(n):
    result = 1
    for i, p in enumerate(primes):
        if p > n:
            break
        k = fac_nup[i][n] * (n + 1) - 2 * fac_nup_sum[i][n]
        result = result * (pow(p, k+1, the_mod) - 1)*inv_tab[p - 1] % the_mod
    return result

print(sum(D(n) for n in range(1, N+1)) % the_mod)

correct_answer = "538319652"
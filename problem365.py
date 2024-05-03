r"""
A huge binomial coefficient
The binomial coefficient $\binom{10^{18}}{10^9}$ is a number with more 
than 9 billion ($9 \times 10^9$) digits.

Let M(n, k, m) denote the binomial coefficient $\binom{n}{k]$ modulo m.

Calculate $\sum M(10^{18}, 10^9, p \cdot q \cdot r)$ for 
1000 < p < q < r and p, q, r prime.
"""

from itertools import combinations, dropwhile
from mod_arith import binom_modp, crt
from primes import primes_lt

primes = list(dropwhile(lambda p: p <= 1000, primes_lt(5000)))
primes_and_binoms = [(p, binom_modp(10**18, 10**9, p)) for p in primes]
zero_mod = [t for t in primes_and_binoms if t[1] == 0]
nonzero_mod = [t for t in primes_and_binoms if t[1] != 0]

print(sum(crt(x) for x in combinations(primes_and_binoms, 3) if any(t[1] != 0 for t in x)))
correct_answer = "162619462356610313"
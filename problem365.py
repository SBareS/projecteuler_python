r"""
A huge binomial coefficient
The binomial coefficient $\binom{10^{18}}{10^9}$ is a number with more 
than 9 billion ($9 \times 10^9$) digits.

Let M(n, k, m) denote the binomial coefficient $\binom{n}{k]$ modulo m.

Calculate $\sum M(10^{18}, 10^9, p \cdot q \cdot r)$ for 
1000 < p < q < r and p, q, r prime.
"""

from itertools import combinations, dropwhile
from time import perf_counter
from mod_arith import binom_modp, crt
from primes import primes_lt

# TODO: make this less sloooow (currently ~2 minutes on my shitty 
# laptop in CPython, and ~25 seconds in PyPy).

primes = list(dropwhile(lambda p: p <= 1000, primes_lt(5000)))
primes_and_binoms = [(p, binom_modp(10**18, 10**9, p)) for p in primes]

print(sum(crt(x) for x in combinations(primes_and_binoms, 3)))
correct_answer = "162619462356610313"
"""
Sum of Squares II
For a positive integer, n, define g(n) to be the maximum perfect square that 
divides n. For example, g(18) = 9, g(19) = 1.

Also define S(N) = g(1) + ... + g(N).
For example, S(10) = 24 and S(100) = 767.

Find S(10^14). Give your answer modulo 1 000 000 007. 
"""

from math import isqrt
from arithfunct import mobius_pp, multfunc_table

N = 10**14
themod = 1_000_000_007

# Similar Mobius-trick to Problem 193, but instead of the mobius function, we 
# need to convolve with a different Dirichlet-inverse given on prime by 
# f(p**k) = p**(2*k - 2)*(p**2 - 1).
# This can again be worked out by rewriting some sums.

def f_pp(pk):
    return pk[0]**(2*pk[1] - 2) * (pk[0]**2 - 1)
f_tab = multfunc_table(f_pp, isqrt(N) + 1)
print(sum(N//k**2 * f_tab[k] % themod for k in range(1, isqrt(N)+1)) % themod)
correct_answer = "94586478"
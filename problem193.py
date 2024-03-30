"""
Squarefree Numbers
A positive integer n is called squarefree, if no square of a prime divides n, 
thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 2^50?
"""

from math import isqrt
from arithfunct import mobius_pp, multfunc_table

# This can be done with a Mobius-PIE trick

N = 2**50
sqrtN = isqrt(N)

mobius_tab = multfunc_table(mobius_pp, sqrtN + 1)

print(sum(N//k**2 * mobius_tab[k] for k in range(1, sqrtN + 1)))
correct_answer = "684465067343069"
r"""
Divisor Square Sum
For a positive integer n, let $\\sigma_2(n)$ be the sum of the squares of its 
divisors. For example,
$$\\sigma_2(10) = 1 + 4 + 25 + 100 = 130$$
Find the sum of all n <= 64 000 000, such that $\\sigma_2(n)$ is a perfect square.
"""

from math import isqrt
from arithfunct import multfunc_table

upper_bound = 64_000_000
sigma2_tab = multfunc_table(lambda pk: (pk[0]**(2*pk[1]+2) - 1)//(pk[0]**2 - 1), upper_bound)
# sigma2_tab = multfunc_table(partial(sigma_nat_pp, a=2), upper_bound) # the lambda above has less overhead

def is_square(n):
    return isqrt(n)**2 == n

print(sum(n for n in range(upper_bound) if is_square(sigma2_tab[n])))
correct_answer = "1922364685"
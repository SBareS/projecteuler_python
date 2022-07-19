"""
Counting fractions in a range
Consider the fraction, n/d, where n and d are positive integers. If n<d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d ≤ 12,000?
"""

from arithfunct import mobius_pp, multfunc_table

N = 12000
mobius_tab = multfunc_table(mobius_pp, N+1)

def n_unreduced_fractions(n):
    # The formula below for the number of fractions in (1/3, 1/2) *with
    # repeats for unreduced fractions* is easy to show with some 
    # pen-and-paper calculation (or one can cheat and check the 
    # pdf-notes for derivation)
    q, r = divmod(n, 6)
    return q * (3*q - 2 + r) + (r == 5)

def n_reduced_fractions(n):
    # Letting F denote the function above, and R this function, 
    # one sees that
    # F(n) == sum(R(n//m) for m in range(1, n+1))
    # Generalized Mobius inversion then gives the following:
    return sum(mobius_tab[m] * n_unreduced_fractions(n // m) for m in range(1, n+1))

print(n_reduced_fractions(N))
correct_answer = "7295372"
"""
Palindromic Sequences

Given an irrational number alpha, let S_alpha(n) be the sequence 
S_alpha(n) = floor(alpha*n) - floor((alpha - 1)*n)
for n >= 1.

It can be proven that for any irrational alpha there exist infinitely many
values of n such that the subsequence 
{S_alpha(1), S_alpha(2), ..., S_alpha(n)} is palindromic.

The first 20 values of n that give a palindromic subsequence for 
alpha = sqrt(31) are: 1, 3, 5, 7, 44, 81, 118, 273, 3158, 9201, 15244, 21287,
133765, 246243, 358721, 829920, 9600319, 27971037, 46341755, 64712473.

Let H_g(alpha) be the sum of the first g values of n for which the 
corresponding subsequence is palindromic.
So H_20(sqrt(31)) = 150243655.

Let T = {2, 3, 5, 6, 7, 8, 10, ..., 1000} be the set of positive integers, not
exceeding 1000, excluding perfect squares. Calculate the sum of 
H_g(sqrt(beta)) for beta in T. Give the last 15 digits of your answer.
"""

from itertools import islice
from math import isqrt
from cfrac import sqrt_cfrac

the_mod = 10**15

# The indices up to which the prefixes are palindromic are the denominators of
# odd-indexed convergents and their preceding semiconvergents, see 
# Kimberling 1998 "Palindromic Sequences from Irrational Numbers" and 
# Komatsu 1999 "On Palindromic Sequences from Irrational Numbers".

def palindromic_prefixes(d):
    q0, q1 = 1, 0
    sgn = +1
    for a in sqrt_cfrac(d):
        if sgn == -1:
            for b in range(1, a+1):
                yield (b*q1 + q0) % the_mod
        q0, q1 = q1, (a*q1 + q0) % the_mod
        sgn = -sgn

result = 0
for d in range(1000 + 1):
    if isqrt(d)**2 == d:
        continue
    result = (result + sum(islice(palindromic_prefixes(d), 100))) % the_mod
print(result)

correct_answer = "888873503555187"
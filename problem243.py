"""
Resilience

A positive fraction whose numerator is less than its denominator is called a 
proper fraction. For any denominator, d, there will be d-1 proper fractions;
for example, with d=12:
1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the
ratio of its proper fractions that are resilient; for example, R(12)=4/11.
In fact, 12 is the smallest denominator having a resilience R(d)<4/10.

Find the smallest denominator d, having a resilience R(d)<15499/94744.
"""

from itertools import accumulate, pairwise
import operator
from arithfunct import euler_phi
import factorization
from primes import primes_lt

prime_bound = 100 #Guesstimate
factorization.generate_default_primes_and_hints(prime_bound)
primes = primes_lt(prime_bound)
primorials = accumulate(primes, operator.mul)

# Per https://oeis.org/A060735, the answer is very likely among these candidates
# (the miniscule difference between phi(n)/(n-1) and (phi(n) + 1)/n is unlikely
# to matter; indeed it turns out not to).
def candidates():
    for x, y in pairwise(primorials):
        yield from range(x, y, x)

for n in candidates():
    if 94744 * euler_phi(n) < 15499*(n - 1):
        print(n)
        break
else:
    print("Ran out of candidates :-(")

correct_result = "892371480"
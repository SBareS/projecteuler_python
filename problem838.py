"""
Not Coprime
 
Problem 838

Let f(N) be the smallest positive integer that is not coprime to any positive
integer n<=N whose least significant digit is 3.

For example f(40) equals to 897=3*13*23 since it is not coprime to any of 
3, 13, 23, 33. By taking the natural logarithm (log to base e) we obtain
ln(f(40)) = ln(897) \\approx 6.799056 when rounded to six digits after the
decimal point.

You are also given $ln(f(2800)) \\approx 715.019337$.

Find f(10^6). Enter its natural logarithm rounded to six digits after the
decimal point.
"""

from collections import Counter
from math import log
import factorization
from factorization import unique_prime_factors
from primes import is_prime

upper_bound = 10**6

factorization.generate_default_hints(upper_bound+1)

# We certainly need all primes ending in a 3...
have_primes = set(p for p in range(3, upper_bound+1, 10) if is_prime(p))
# ...but other primes could occur in composite numbers ending in 3 as well!
todo = [unique_prime_factors(n) for n in range(3, upper_bound+1, 10) if not is_prime(n)]

# Powers of primes have to be handled separately
for ps in todo:
    if len(ps) == 1:
        have_primes.add(ps[0])
todo = [ps for ps in todo if not any(p in have_primes for p in ps)]

# For the rest the following heuristic happens to work: Greedily keep picking 
# the prime occurring in the most different numbers not handled yet. This is
# sort of an accident; it may fail for other N.
# TODO: Make a solution that is guaranteed to work for all N?
while todo:
    ctr = Counter(p for ps in todo for p in ps)
    have_primes.add(max(ctr, key=ctr.get))
    todo = [ps for ps in todo if not any(p in have_primes for p in ps)]

result = sum(log(p) for p in have_primes)
print(f"{result:.6f}")

correct_answer = "250591.442792"
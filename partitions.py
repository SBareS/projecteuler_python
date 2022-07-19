"""Contains functions for counting partitions."""

from comb_it import integer_partitions
from functools import cache
from itertools import count, takewhile

def _gpns_and_signs():
    sign = 1
    for k in count(1):
        yield (k*(3*k-1))//2, sign
        yield (k*(3*k+1))//2, sign
        sign *= -1

@cache
def n_partitions(n):
    if n == 0:
        return 1
    result = 0
    rec_cases = list(takewhile(lambda x: x[0] <= n, _gpns_and_signs()))
    # We loop through rec_cases in reverse so as to do the recursive 
    # calls on the smaller values first. This decreases the number of 
    # memo-misses for the small-offset recursive calls, and also makes
    # it less likely that we hit the recursion limit.
    for g, s in reversed(rec_cases):
        result += s * n_partitions(n - g)
    return result
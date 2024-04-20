"""
Chip Defects
k defects are randomly distributed amongst n integrated-circuit chips produced
by a factory (any number of defects may be found on a chip and each defect is
independent of the other defects).

Let p(k, n) represent the probability that there is a chip with at least 3 
defects. For instance p(3, 7) = 0.0204081633.

Find p(20 000, 1 000 000) and give your answer rounded to 10 decimal places in
the form 0.abcdefghij.
"""

from math import prod

# Finding the probability p(k, n, r) that there are exactly r chips with 2 
# defects and k-r chips with 1 defect is a simple combinatorial problem
# Then just compute 1 - p(k, n, 0) - p(k, n, 1) - ... - p(k, n, k//2).
# This is further simplified by p(k, n, r)/p(k, n, r-1) being a simple 
# rational function.

k, n = 20_000, 1_000_000
p = 1

q = prod((n-i)/n for i in range(k)) # p(k, n, 0)
p -= q

for r in range(1, k//2 + 1):
    q *= (k - 2*r + 1)*(k - 2*r + 2)/(2*r*(n - k + r)) # p(k, n, r)/p(k, n, r-1)
    p -= q

print(f"{p:.10f}")
correct_answer = "0.7311720251"
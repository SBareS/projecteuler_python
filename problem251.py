"""
Cardano Triplets

A triplet of positive integers (a, b, c) is called a Cardano Triplet if it 
satisfies the condition: 
$$\\sqrt[3]{a + b\\sqrt{c}} + \\sqrt[3]{a - b\\sqrt{c}} = 1$$

For example, (2, 1, 5) is a Cardano Triplet.

There exist 149 Cardano Triplets for which a + b + c <= 1000.

Find how many Cardano Triplets exist such that a + b + c <= 110000000. 
"""

# The equation is equivalent to
# 8a^3 + 15a^2 + 6a - 1 = 27 b^2 c
# One quickly finds that a must be of the form 3k + 2 for the left-hand side
# to be a multiple of 27, giving the parametrization
# a = 3k + 2,      b^2 c = (k + 1)^2 * (8k + 5)
# Instead of iterating over a and factoring, it is faster to iterate over the
# square and square-free parts of b^2 * c.

from itertools import repeat
from math import isqrt

upper_bound = 110_000_000


# Tabulate odd squarefree numbers
is_squarefree = [True] * (upper_bound//2 + 1)
for sqpart in range(3, isqrt(upper_bound) + 1, 2):
    if not is_squarefree[sqpart // 2]:
        continue
    #for i in range(1, upper_bound//sqpart**2 + 1, 2):
    #    is_squarefree[i*sqpart**2 // 2] = False
    is_squarefree[sqpart**2//2 : upper_bound//2 + 1 : sqpart**2] = repeat(False, len(range(sqpart**2//2, upper_bound//2 + 1, sqpart**2)))

result = 0
for sfpart in range(5, upper_bound + 1, 8):
    if not is_squarefree[sfpart // 2]:
        continue
    d = isqrt(upper_bound // sfpart)
    for sqpart in range(1, upper_bound + 1, 2):
        a = (1 + 3 * sqpart**2 * sfpart) // 8
        b = (3 * sqpart + sqpart**3 * sfpart) // 8
        if a + b//d + sfpart > upper_bound:
            break
        for sqpart in range(1, min(b, d) + 1):
            result += b % sqpart == 0 and a + b//sqpart + sfpart * sqpart**2 <= upper_bound

print(result)

correct_answer = "18946051"
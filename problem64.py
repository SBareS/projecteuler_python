"""
Odd period square roots
All square roots are periodic when written as continued fractions and
can be written in the form:
$$\sqrt{N} = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3+\dots}}}$$
For example, let us consider
$$\sqrt{23} = 4 + \sqrt{23} - 4 = 4 + \frac{1}{\frac{1}{\sqrt{23}-4}}
= 4 + \frac{1}{1 + \frac{\sqrt{23}-3}{7}}$$
If we continue we would get the following expansion:
$$\sqrt{23}=4+\frac{1}{1+\frac{1}{3+\frac{1}{1+\frac{1}{8+\dots}}}}$$
The process can be summarised as follows:
[...]
It can be seen that the sequence is repeating. For conciseness, we use
the notation $\sqrt{23} = [4; (1,3,1,8)]$, to indicate that the block
(1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square
roots are:
[...]
Exactly four continued fractions, for N<=13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
"""

from itertools import takewhile
from math import isqrt
from cfrac import sqrt_cfrac


def sqrt_cfrac_period(n):
    # last term in the periodic bit turns out to always be 2*isqrt(n)
    a0 = isqrt(n)
    return sum(1 for _ in takewhile(lambda a: a != 2*a0, sqrt_cfrac(n)))

def is_square(n):
    return isqrt(n)**2 == n

print(sum(not is_square(n) and sqrt_cfrac_period(n) % 2 == 1 for n in range(1, 10**4 + 1)))
correct_answer = "1322"
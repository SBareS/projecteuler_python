r"""
Convergents of e
The square root of 2 can be written as an infinite continued fraction.
$$\sqrt{2} = \frac{1}{2 + \frac{1}{2 + \dots}}$$
The infinite continued fraction can be written, $\sqrt{2} = [1; (2)]$,
indicates that 2 repeats ad infinitum. In a similar way, 
$\sqrt{23} = [4; (1,3,1,8)]$.

It turns out that the sequence of partial values of continued fractions
for square roots provide the best rational approximations. Let us consider
the convergents for $\sqrt{2}$
[...]
Hence the sequence of the first ten convergents for $\sqrt{2}$ are:
[...]
What is most surprising is that the important mathematical constant,
$$e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, \dots, 1, 2k, 1, \dots].$$

The first ten terms in the sequence of convergents for e are:
$$2, 3, \frac{8}{3}, \frac{11}{4}, \frac{19}{7}, \frac{87}{32},
\frac{106}{39}, \frac{193}{71}, \frac{1264}{465}, \frac{1457}{536},
\dots$$
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""

from itertools import count
from cfrac import convergents
from digits import digits
from sequences import nth

def e_cfrac():
    yield 2
    for n in count(1):
        yield from [1, 2*n, 1]

print(sum(digits(nth(convergents(e_cfrac()), 100-1)[0])))
correct_answer = "272"
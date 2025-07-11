r"""
Diophantine equation
Consider quadratic Diophantine equations of the form:

$$x^2 - Dy^2 = 1$$

For example, when D=13, the minimal solution in x is 
$649^2 - 13\\times180^2 = 1$.

It can be assumed that there are no solutions in positive integers when
D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

$$32 - 2\\times2^2 = 1$$
$$22 - 3\\times1^2 = 1$$
$$92 - 5\\times4^2 = 1$$
$$52 - 6\\times2^2 = 1$$
$$82 - 7\\times3^2 = 1$$

Hence, by considering minimal solutions in x for D ≤ 7, the largest x
is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the
largest value of x is obtained.
"""

from math import isqrt
from cfrac import minimal_pell_soln

non_squares = filter(lambda x: isqrt(x)**2 != x, range(1001))
print(max(non_squares, key=lambda d: minimal_pell_soln(d)[0]))
correct_answer = "661"
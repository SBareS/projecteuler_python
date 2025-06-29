r"""
For a non-negative integer $k$, define
$$E_k(q) = \\sum_{n=1}^\infty \\sigma_k(n)q^n$$
where $\\sigma_k(n) = \\sum_{d\divides n}d^k$ is the sum of the $k$-th powers of
the positive divisors of $n$.

It can be shown that, for every $k$, the series converges for any $0 < q < 1$.

For example,
$E_1(1 - \\frac{1}{2^4}) = 3.872155809243e2$
$E_3(1 - \\frac{1}{2^8}) = 2.767385314772e10$
$E_7(1 - \\frac{1}{2^{15}}) = 6.725803486744e39$

All the above values are given in scientific notation rounded to twelve digits after the decimal point.

Find the value of $E_{15}(1 - \\frac{1}{2^{25}})$.
Give the answer in scientific notation rounded to twelve digits after the decimal point.
"""

# I <3 modular forms

from math import pi

k = 16
Bk = -3617/510
t = 2**-25

zoveri = (t + t**2/2)/(2*pi)    # Taylor approximation to -log(1-t)/(2*pi)
automorphy = zoveri**-k         # From modular transformation property of Ek
Ek_of_q = -Bk/(2*k)*automorphy  # q is now tiny, so only need constant term

# Convert from "#.############e+###" to "#.############e###"
answer = ''.join(f"{Ek_of_q:.12e}".split('+'))
print(answer)
correct_answer = "3.376792776502e132"
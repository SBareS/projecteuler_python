r"""
Largest Roots of Cubic Polynomials
Let $a_n$ be the largest real root of a polynomial $x^3 - 2^n x^2 + n$.
For example, $a_2 = 3.86619826...$ Find the last eight digits of
\sum_{i=1}^{30} \floor{a_i^{987654321}}.

Note:
represents the floor function.
"""

from matrix import Mat33
from mod_arith import ZMod


N = 987654321
themod = 10**8
ZM = ZMod(themod)
Mat = Mat33(ZM)

# Let a, b, c be the three roots. Then f(k) = a**k + b**k + c**k satisfies
# f(0) = 3
# f(1) = 2**n
# f(2) = (a + b + c)**2 - 2(a*b + b*c + c*d) = 2**(2*n)
# f(k) = 2**n * f(k-1) - n*f(k-3)
# Further, if a is the largest root, then 0 < b**N + c**N < 1 for N large, so
# floor (a**N) = f(N) - 1.

result = 0
for i in range(1, 31):
    themat = Mat(ZM(2)**i, ZM(0), -ZM(i),
                 ZM(1), ZM(0), ZM(0),
                 ZM(0), ZM(1), ZM(0)
                 )**N
    result += themat[6] * ZM(2)**(2*i) + themat[7] * ZM(2)**i + themat[8] * 3 - ZM(1)
print(result)
correct_answer = "28010159"
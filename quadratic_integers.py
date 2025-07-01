"""
Contains some simple helpers for calculations with quadratic integers.
"""

from numbers import Complex

from mod_arith import sqrt_modp

def prime_sum_of_squares(p):
    """Given a prime p not congruent to 3 modulo 4, returns a pair of integers
    (a, b) such that 0 < a <= b and a**2 + b**2 == p."""
    if p == 2:
        return (1, 1)
    if p % 4 == 3:
        raise ValueError("Cannot write primes congruent to 3 modulo 4 as a sum of two squares!")
    
    a = sqrt_modp(-1, p)[0]
    b = p
    while b**2 > p:
        a, b = b % a, a
    return a, b


# This Gaussian integer class is not presently used for anything. It was made 
# for Problem 273, but doing all the multiplications manually instead sped up
# everything by a factor of 2 (not surprising, as method calls are sloooow)
class Zi(tuple[int, int], Complex):
    def __new__(cls, a, b):
        return super().__new__(cls, (a, b))
    def real(self):
        return self[0]
    def imag(self):
        return self[1]
    def conjugate(self):
        return Zi(self[0], -self[1])
    def __add__(self, other):
        a, b = self
        c, d = other if isinstance(other, Zi) else other, 0
        return Zi(a+c, b+d)
    def __radd__(self, other):
        a, b = other if isinstance(other, Zi) else other, 0
        c, d = self
        return Zi(a+c, b+d)
    def __sub__(self, other):
        a, b = self
        c, d = other if isinstance(other, Zi) else (other, 0)
        return Zi(a-c, b-d)
    def __rsub__(self, other):
        a, b = other if isinstance(other, Zi) else (other, 0)
        c, d = self
        return Zi(a-c, b-d)
    def __neg__(self):
        a, b = self
        return Zi(-a, -b)
    def __mul__(self, other):
        a, b = self
        c, d = other if isinstance(other, Zi) else (other, 0)
        return Zi(a*c - b*d, a*d + b*c)
    def __rmul__(self, other):
        a, b = other if isinstance(other, Zi) else (other, 0)
        c, d = self
        return Zi(a*c - b*d, a*d + b*c)
    def cast(x):
        return x if isinstance(x, Zi) else Zi(x, 0)
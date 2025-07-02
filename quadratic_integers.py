"""
Contains some simple helpers for calculations with quadratic integers.
"""

from math import sqrt
from numbers import Complex, Integral

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
    __slots__ = ()
    def __new__(cls, a, b):
        return super().__new__(cls, (a, b))
    def __str__(self):
        a, b = self
        if a == 0:
            return f"{b}j"
        return f"{a}{b:+}j"
    @property
    def real(self):
        return self[0]
    @property
    def imag(self):
        return self[1]
    def conjugate(self):
        return Zi(self[0], -self[1])
    def __complex__(self):
        return complex(self[0], self[1])
    def __eq__(self, other):
        return self[0] == other.real and self[1] == other.imag
    def __neq__(self, other):
        return self[0] != other.real or self[1] != other.imag
    def __abs__(self):
        return sqrt(self[0]**2 + self[1]**2)
    def __bool__(self):
        return self[0] != 0 or self[1] != 0
    def __add__(self, other):
        a, b = self
        c, d = other.real, other.imag
        return Zi(a+c, b+d)
    def __radd__(self, other):
        a, b = other.real, other.imag
        c, d = self
        return Zi(a+c, b+d)
    def __sub__(self, other):
        a, b = self
        c, d = other.real, other.imag
        return Zi(a-c, b-d)
    def __rsub__(self, other):
        a, b = other.real, other.imag
        c, d = self
        return Zi(a-c, b-d)
    def __neg__(self):
        return Zi(-self[0], -self[1])
    def __mul__(self, other):
        a, b = self
        c, d = other.real, other.imag
        return Zi(a*c - b*d, a*d + b*c)
    def __rmul__(self, other):
        a, b = other.real, other.imag
        c, d = self
        return Zi(a*c - b*d, a*d + b*c)
    def __truediv__(self, other):
        return complex(self) / complex(other)
    def __rtruediv__(self, other):
        return complex(other) / complex(self)
    def __pow__(self, exponent):
        if not isinstance(exponent, Integral) or exponent < 0:
            return pow(complex(self), exponent)
        result = Zi(1, 0)
        selfpow = self
        while exponent:
            if exponent & 1:
                result *= selfpow
            exponent >>= 1
            selfpow *= selfpow
        return result
    def __rpow__(self, base):
        return pow(base, complex(self))
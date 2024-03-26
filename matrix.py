"""Contains simple helpers for matrix algebra. For now just 2x2 matrices"""

from functools import cache
from typing import Tuple

@cache
def Mat22(t) -> type:
    class Mat22t(Tuple[t, t, t, t]):
        def __new__(cls, a, b, c, d):
            return tuple.__new__(cls, (a, b, c, d))
        def __add__(self, other):
            return Mat22t(*map(t.__add__, self, other))
        def __radd__(self, other):
            return Mat22t(*map(t.__radd__, self, other))
        def __sub__(self, other):
            return Mat22t(*map(t.__sub__, self, other))
        def __rsub__(self, other):
            return Mat22t(*map(t.__rsub__, self, other))
        def __mul__(self, other):
            a1, b1, c1, d1 = self
            a2, b2, c2, d2 = other
            return Mat22t(a1*a2 + b1*c2, a1*b2 + b1*d2, c1*a2 + d1*c2, c1*b2 + d1*d2)
        def __rmul__(self, other):
            a1, b1, c1, d1 = other
            a2, b2, c2, d2 = self
            return Mat22t(a1*a2 + b1*c2, a1*b2 + b1*d2, c1*a2 + d1*c2, c1*b2 + d1*d2)
        def __pow__(self, n):
            if n == 0:
                return self.identity
            if n < 0:
                raise NotImplementedError
            if n % 2 == 0:
                square = self * self
                return square.__pow__(n // 2)
            return self * self.__pow__(n-1)
        def __truediv__(self, other):
            raise NotImplementedError
        def __rtruediv__(self, other):
            raise NotImplementedError
    
    Mat22t.identity = Mat22t(1, 0, 0, 1)
    
    Mat22t.__name__ = f"Mat22({t})"
    Mat22t.__qualname__ = ''.join([*Mat22t.__qualname__.split('.')[:-3], f'Mat22({t})'])
    return Mat22t
    
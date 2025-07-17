"""
Contains some helper functions for calculations with polynomials (so far only 
over F2).

Polynomials over F2 are treated as integers (bit strings) with the 1s digit 
representing the X^0 term, the 2s digit representing the X^1 term and so on.
"""

from functools import reduce
import operator


def polymul_f2(f: int, g: int) -> int:
    """Multiply two polynomials over F2."""
    if g > f:
        f, g = g, f
    return reduce(operator.xor, (f << i for i in range(g.bit_length()) if g & (1<<i)), 0)
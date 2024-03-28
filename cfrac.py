"""Contains functions for dealing with continued fractions. Also 
contains some functions for solving Pell's equation. Also contains some
functions for dealing with Farey sequences."""

from fractions import Fraction
from functools import wraps
from itertools import islice, starmap
from math import floor, isqrt

def _convert_numden_seq(gen):
    @wraps(gen)
    def wrapper(*args, as_fraction=False, **kwargs):
        g = gen(*args, **kwargs)
        if as_fraction:
            return starmap(Fraction, g)
        else:
            return g
    return wrapper

def _convert_cfrac_seq(gen):
    @wraps(gen)
    def wrapper(*args, as_convergents=False, **kwargs):
        g = gen(*args, **kwargs)
        if as_convergents:
            return convergents(g)
        else:
            return g
    return wrapper

@_convert_cfrac_seq
def cfrac(x):
    """Given a number x = [a0; a1, a2, ...], yields the terms 
    a0, a1, a2, ... in the continued fraction expansion of x."""
    while True:
        a = floor(x)
        yield a
        x -= a
        if x == 0:
            break
        x = 1/x

@_convert_numden_seq
def convergents(cf_seq):
    """Yields the convergets of the continued fraction given by the 
    integer sequence cf_seq as (numerator, denominator) pairs. If the
    kwarg as_fraction is set to True, returns Fraction objects instead."""
    try:
        p0, q0 = next(cf_seq), 1
        yield p0, q0
        a = next(cf_seq)
        # p0 + 1/a = (p0*a + 1)/a
        p1, q1 = a*p0 + 1, a
        yield p1, q1
    except StopIteration:
        return
    for a in cf_seq:
        p0, q0, p1, q1 = p1, q1, a*p1 + p0, a*q1 + q0
        yield p1, q1

@_convert_cfrac_seq
def sqrt_cfrac(n):
    """Yields the continued fraction expansion of sqrt(n) for a positive 
    integer n."""
    a0 = isqrt(n)
    a, d, m = a0, 1, 0
    yield a
    if a*a == n:
        return 
    
    # n is a non-square, so sqrt(n) is irrational, i.e. the continued 
    # fraction expansion is infinite
    while True:
        # This recursion can be obtained rather easily with some 
        # pen-and-paper calculations in the field Q(sqrt(d))
        m = d*a - m
        d = (n - m*m)//d
        a = (a0 + m)//d
        yield a

def minimal_pell_soln(d):
    """Returns the minimal non-trivial solution (x, y) to Pell's 
    equation x**2 - d*y**2 = 1 where d is a positive, non-square integer"""
    for (x, y) in islice(sqrt_cfrac(d, as_convergents=True), 1, None):
        if x**2 - d*y**2 == 1:
            return (x, y)
    else:
        raise ValueError("d must not be a square")

def _farey_sum(a, b):
    na, da = a
    nb, db = b
    return (na+nb, da+db)

@_convert_numden_seq
def farey_sequence(n, L=(0,1), R=(1,1), *, include_bounds=False):
    """Returns the Farey sequence of order n, i.e. the ordered sequnce 
    of all fractions in the interval (0, 1) (note that the endpoints 
    are not included, unlike the most common definition) with 
    denominator at most n. The result is given as a generator of (numerator, denominator)
    pairs. Optionally, different bounds than ((0,1), (1,1)) can be 
    given. If you want to include the bounds, set the include_bounds to True"""
    if include_bounds:
        yield L

    # Unfortunately, we have to manage the stack manually
    # to avoid the recursion limit
    M = _farey_sum(L, R)
    stack = [(L, M, R, 0)]
    while stack:
        L, M, R, step = stack.pop()
        if step == 0:
            LM = _farey_sum(L, M)
            stack.append((L, M, R, 1))
            if LM[1] <= n:
                stack.append((L, LM, M, 0))
        elif step == 1:
            MR = _farey_sum(M, R)
            yield M
            if MR[1] <= n:
                stack.append((M, MR, R, 0))

    if include_bounds:
        yield R

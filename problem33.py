"""
Digit cancelling fractions
The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common 
terms, find the value of the denominator.
"""

from fractions import Fraction
from math import prod

from digits import digits


def cancellable(n, d):
    n_over_d = Fraction(n, d)
    n_digs = digits(n)
    d_digs = digits(d)
    assert len(n_digs) == len(d_digs) == 2
    for i in [0, 1]:
        for j in [0, 1]:
            if n_digs[i] == d_digs[j] and d_digs[1-j] != 0:
                cancelled = Fraction(n_digs[1-i], d_digs[1-j])
                if cancelled == n_over_d:
                    return True
    return False

cancellable_fractions = []
for n in range(10, 99):
    if n % 10 == 0:
        continue
    for d in range(n+1, 100):
        if d % 10 == 0:
            continue
        n_over_d = Fraction(n, d)
        if n_over_d not in cancellable_fractions and cancellable(n, d):
            cancellable_fractions.append(n_over_d)

assert len(cancellable_fractions) == 4
print(prod(cancellable_fractions).denominator)
correct_answer = "100"
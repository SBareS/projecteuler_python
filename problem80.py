"""
Square root digital expansion
It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square 
roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum
of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational
square roots.
"""

from digits import digits

from math import isqrt


print(sum(d for n in range(1, 101) if isqrt(n)**2 != n for d in digits(isqrt(n * 10**202))[:100]))
correct_answer = "40886"
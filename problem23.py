"""
Non-abundant sums
A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as 
the sum of two abundant numbers.
"""

from functools import cache
import factorization
from arithfunct import sigma_nat


N = 28123
factorization.generate_default_hints(N+1)

@cache
def is_abundant(n):
    return sigma_nat(n) > 2*n

abundant_numbers = [n for n in range(1, N) if is_abundant(n)]
def is_abundant_sum(n):
    for x in abundant_numbers:
        if x >= n:
            return False
        if is_abundant(n - x):
            return True
    return False

print(sum(i for i in range(1, N) if not is_abundant_sum(i)))
correct_answer = "4179871"
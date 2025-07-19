"""
Singleton Difference

The positive integers, x, y, and z, are consecutive terms of an arithmetic 
progression. Given that n is a positive integer, the equation, 
x^2 - y^2 - z^2 = n, has exactly one solution when n = 20:
13^2 - 10^2 - 7^2 = 20.
In fact there are twenty-five values of n below one hundred for which the 
equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
"""

from primes import primes_lt


upper_bound = 50_000_000

# As in problem 135, we're counting representations of n on the form 
# (4*diff - y)*y. However, instead of counting directly, we can use some 
# simple divisor counting. The numbers in question are then 4, 16, 
# 4*(odd prime), 16*(odd prime) as well as primes congruent to 3 modulo 4.
primes = primes_lt(upper_bound)
result = 2 #4 and 16
for p in primes:
    if p == 2:
        continue
    result += 4*p < upper_bound
    result += 16*p < upper_bound
    result += p % 4 == 3

print(result)        

correct_answer = "2544559"
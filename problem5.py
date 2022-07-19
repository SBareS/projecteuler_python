"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""


from math import lcm


print(lcm(*range(1, 20+1)))
correct_answer = "232792560"
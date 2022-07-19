"""
Permuted multiples
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 
6x, contain the same digits.
"""

from math import floor

# Thid is a well-known mathematical curiosity which stems from the fact
# that 10 is a primitive root modulo 7.
print(floor(10**6 / 7))
correct_answer = "142857"
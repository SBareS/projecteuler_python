"""
Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which,
$$a^2 + b^2 = c^2$$
For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2.$
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import prod


def find_tripple(N):
    for a in range(1, N//3 + 1):
        for b in range(a+1, (N-a)//2 + 1):
            c = N - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)

print(prod(find_tripple(1000)))
correct_answer = "31875000"
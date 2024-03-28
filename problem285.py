"""
Pythagorean Odds
Albert chooses a positive integer k, then two real numbers a, b are 
randomly chosen in the interval [0, 1] with uniform distribution.
The square root of the sum (k*a + 1)^2 + (k*b + 1)^2 is then computed and
rounded to the nearest integer. If the result is equal to k, he scores k 
points; otherwise he scores nothing.

For example, if k = 6, a = 0.2, and b = 0.85, then then 
(k*a + 1)^2 + (k*b + 1)^2 = 42.05.
The square root of 42.05 is 6.484... and when rounded to the nearest integer,
it becomes 6. This is equal to k, so he scores 6 points.

It can be shown that if he plays 10 turns with k = 1, k = 2, ..., k = 10, the
expected value of his total score, rounded to five decimal places, is 10.20914.

If he plays 10^5 turns with k = 1, k = 2, ..., k = 10^5, what is the expected
value of his total score, rounded to five decimal places?
"""

from math import pi, sqrt, asin

turns = 10**5

# The probability of winning the k-game has a nice geometric interpretation: 
# it is the area of an annular arc of radii (k-1/2, k+1/2) within the square
# [1, k+1]^2, divided by the area k^2 of the square. The case k=1 needs to 
# be handled separately, as the inner arc of the annulus is outside the square
# in this case.

# Area of the intersection of a circle of radius r with [1, infty)^2
def area(r):
    return (pi/4 - asin(1/r)) * r**2 - sqrt(r**2 - 1) + 1

result = sum((area(k+.5) - area(k - 0.5))/k for k in range(2, turns+1))
result += area(1.5) # Handle the case k=1 separately

print(f"{result:.5f}")
correct_answer = "157055.80999"
"""
Pythagorean Ant
Dave is doing his homework on the balcony and, preparing a presentation
about Pythagorean triangles, has just cut out a triangle with side
lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind
blows the triangle down into the garden.
Another gust blows a small ant straight onto this triangle. The poor ant
is completely disoriented and starts to crawl straight ahead in random
direction in order to get back into the grass.

Assuming that all possible positions of the ant within the triangle and
all possible directions of moving on are equiprobable, what is the
probability that the ant leaves the triangle along its longest side?
Give your answer rounded to 10 digits after the decimal point.
"""

from math import atan, log, pi

# The integral in question can be computed exactly, either by hand or
# by CAS. The below is simply copy-pasted output from sagemath.
result = 1/24*(18*pi - 12*atan(4/3) - 12*atan(3/4) - 25*log(5) + 9*log(3) + 32*log(2))/pi
print(f"{result:.10f}")
correct_answer = "0.3916721504"
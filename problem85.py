"""
Counting Rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles:

(image)

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.
"""

# There are comb(n+1, 2)*comb(m+1, 2) ways of picking two horizontal and two 
# vertical lines forming a rectangle in an n by m grid. Simply find n, m 
# getting this as close to two million as possible.

from math import ceil, floor, sqrt

target = 2_000_000

best_area = 0
best_diff = target

for n in range(1, ceil((-1 + sqrt(1 + 8*target))/2) + 1):
    x = (-1 + sqrt(1 + 16*target/(n*(n+1)))) / 2
    for m in (floor(x), ceil(x)):
        n_squares = (n + 1) * n * (m + 1) * m // 4
        diff = abs(n_squares - target)
        if diff < best_diff:
            best_diff, best_area = diff, m*n

print(best_area)
correct_answer = "2772"
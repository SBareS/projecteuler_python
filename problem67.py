"""
Maximum path sum II
By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle 
with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not 
possible to try every route to solve this problem, as there are 299 
altogether! If you could check one trillion ($10^{12}$) routes every 
second it would take over twenty billion years to check them all. There
is an efficient algorithm to solve it. ;o)
"""

from functools import cache

with open("data/p067_triangle.txt") as file:
    triangle = list(map(lambda row: list(map(int, row.split())), 
                    file.readlines()))

@cache  # This almost feels like cheating, lol.
def max_starting_from(row, col):
    current = triangle[row][col]
    
    if row == len(triangle) - 1:
        return current
    
    next = max(
        max_starting_from(row+1, col), 
        max_starting_from(row+1, col+1))
    
    return current + next

print(max_starting_from(0, 0))
correct_answer = "7273"
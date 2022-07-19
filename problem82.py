"""
Path sum: three ways
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell
in the left column and finishing in any cell in the right column, and
only moving up, down, and right, is indicated in red and bold; the sum
is equal to 994.
[...]
Find the minimal path sum from the left column to the right column in
matrix.txt (right click and "Save Link/Target As..."), a 31K text file
containing an 80 by 80 matrix.
"""

from functools import cache


with open("data/p082_matrix.txt") as file:
    matrix = [[int(cell) for cell in row.split(',')] for row in file.readlines()]

height = len(matrix)
width = len(matrix[0])


def path_sum_three_ways(r, c):
    @cache
    def rec(r, c):
        if c == width - 1:
            return matrix[r][c]
        
        rec_results = []
        sum_down = 0
        for r1 in range(r, height):
            sum_down += matrix[r1][c]
            rec_results.append(rec(r1, c+1) + sum_down)
        sum_up = matrix[r][c]
        for r1 in range(r-1, -1, -1):
            sum_up += matrix[r1][c]
            rec_results.append(rec(r1, c+1) + sum_up)
        
        return min(rec_results)
    return min(rec(r, 0) for r in range(height))

print(path_sum_three_ways(0, 0))
correct_answer = "260324"
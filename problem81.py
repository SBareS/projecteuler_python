"""
Path sum: two ways
In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by only moving to the right and down, is indicated in
bold red and is equal to 2427.
[...]
Find the minimal path sum from the top left to the bottom right by only
moving right and down in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing an 80 by 80 matrix.
"""

from functools import cache


with open("data/p081_matrix.txt") as file:
    matrix = [[int(cell) for cell in row.split(',')] for row in file.readlines()]

height = len(matrix)
width = len(matrix[0])

@cache
def path_sum_two_ways(r, c):
    if (r, c) == (height - 1, width - 1):
        return matrix[r][c]
    
    rec_results = []
    if r < height - 1:
        rec_results.append(path_sum_two_ways(r + 1, c))
    if c < width - 1:
        rec_results.append(path_sum_two_ways(r, c + 1))
    
    return min(rec_results) + matrix[r][c]

print(path_sum_two_ways(0, 0))
correct_answer = "427337"
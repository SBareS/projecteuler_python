"""
Path sum: four ways
NOTE: This problem is a significantly more challenging version of
Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by moving left, right, up, and down, is indicated in
bold red and is equal to 2297.
[...]
Find the minimal path sum from the top left to the bottom right by
moving left, right, up, and down in matrix.txt (right click and "Save
Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

from collections import defaultdict
from itertools import product

from dgraph import WeightedHalfEdge, dijkstra


with open("data/p083_matrix.txt") as file:
    matrix = [[int(cell) for cell in row.split(',')] for row in file.readlines()]

height = len(matrix)
width = len(matrix[0])

# Unlike problems 81 and 82, this one can't (as far as I can tell) be 
# solved using simple dynamic programming. Instead, we use the full-
# blown dijkstra-algorithm.
graph = defaultdict(set, {
    "source": {WeightedHalfEdge((0,0), 0)},
    (height-1, width-1): {WeightedHalfEdge("goal", matrix[height-1][width-1])},
    "goal": set()
    })
for r, c in product(range(height), range(width)):
    edges = set()
    weight = matrix[r][c]
    if r > 0:
        edges.add(WeightedHalfEdge((r - 1, c), weight))
    if c > 0:
        edges.add(WeightedHalfEdge((r, c - 1), weight))
    if r < height - 1:
        edges.add(WeightedHalfEdge((r + 1, c), weight))
    if c < width - 1:
        edges.add(WeightedHalfEdge((r, c + 1), weight))
    graph[(r, c)] |= edges

dist, prev = dijkstra(graph, "source", "goal")
print(dist["goal"])
correct_answer = "425185"
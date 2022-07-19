"""
Integer right triangles
If p is the perimeter of a right angle triangle with integral length 
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from pyth_triples import prim_pyth_triples_dfs


max_perim = 1000

n_solutions = (max_perim + 1) * [0]

for a, b, c in prim_pyth_triples_dfs((3, 4, 5), max_perim=max_perim):
    p = a + b + c
    for pp in range(p, max_perim, p):
        n_solutions[pp] += 1

print(max((p for p in range(max_perim+1)), key=n_solutions.__getitem__))
correct_answer = "840"
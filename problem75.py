"""
Singular integer right triangles
It turns out that 12 cm is the smallest length of wire that can be bent
to form an integer sided right angle triangle in exactly one way, but 
there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form
an integer sided right angle triangle, and other lengths allow more
than one solution to be found; for example, using 120 cm it is possible
to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of 
L ≤ 1,500,000 can exactly one integer sided right angle triangle
be formed?
"""

from collections import Counter
from pyth_triples import prim_pyth_triples_dfs

N = 1_500_000

n_pyth_tripes_with_perim = [0] * (N+1)

for a, b, c in prim_pyth_triples_dfs(max_perim=N):
    prim_perim = a + b + c
    for perim in range(prim_perim, N+1, prim_perim):
        n_pyth_tripes_with_perim[perim] += 1

print(sum(n == 1 for n in n_pyth_tripes_with_perim))
correct_answer = "161667"
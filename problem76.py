"""
Counting summations
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""

from functools import cache
from itertools import count, takewhile

from partitions import n_partitions

print(n_partitions(100)-1)  # mius one to exclude the trivial partition
correct_answer = "190569291"
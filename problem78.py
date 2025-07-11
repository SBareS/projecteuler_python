"""
Coin partitions
Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into 
piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

from itertools import count

from partitions import n_partitions

for n in count():
    if n_partitions(n) % 10**6 == 0:
        result = n
        break

print(result)
correct_answer = "55374"
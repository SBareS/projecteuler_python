"""
Pandigital multiples
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 
4, and 5, giving the pandigital, 918273645, which is the concatenated 
product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where 
n > 1?
"""

from itertools import accumulate, chain, permutations

from comb_it import integer_partitions
from digits import undigits

slices = []
for p in integer_partitions(9):
    if len(p) == 1:
        # Skip; the number should be cut in more than one piece
        continue
    if p[-1] - p[0] > 1:
        # Skip; the number of digits in the pieces 
        # can at most differ by one
        continue
    slice_ends = list(accumulate(p))
    slice_starts = chain([0], slice_ends)
    slices.append(list(zip(slice_starts, slice_ends)))

def find_answer():
    for digs in permutations(range(9, 0, -1)):
        for slice in slices:
            subdigs = [undigits(digs[i:j]) for i, j in slice]
            if all(i*subdigs[0] == subdig for i, subdig in enumerate(subdigs, 1)):
                return undigits(digs)

print(find_answer())
correct_answer = "932718654"
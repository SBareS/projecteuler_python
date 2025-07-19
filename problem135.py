"""
Same Differences

Given the positive integers, x, y, and z, are consecutive terms of an 
arithmetic progression, the least value of the positive integer, n, for which 
the equation, x^2 - y^2 - z^2 = n, has exactly two solutions is n = 27:
34^2 - 27^2 - 20^2 = 12^2 - 9^2 - 6^2 = 27.
It turns out that 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct 
solutions?
"""

# Count representations of n as (y + diff)**2 - y**2 - (y - diff)**2 
# = (4*diff - y)*y by simply... counting! Loop over y and diff, 
# rather than n, obviously.

upper_bound = 1_000_000
representations = [0] * upper_bound

for y in range(1, upper_bound):
    for diff in range(y//4+1, min(y, (upper_bound + y**2 + 4*y - 1)//(4*y))):
        representations[(4*diff - y)*y] += 1

print(sum(r == 10 for r in representations))

correct_answer = "4989"
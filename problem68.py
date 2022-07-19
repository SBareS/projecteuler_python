"""
Magic 5-gon ring
Consider the following "magic" 3-gon ring, filled with the numbers 1 
to 6, and each line adding to nine.
[...]
Working clockwise, and starting from the group of three with the 
numerically lowest external node (4,3,2 in this example), each solution
can be described uniquely. For example, the above solution can be
described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10,
11, and 12. There are eight solutions in total.

Total	Solution Set
9	    4,2,3; 5,3,1; 6,1,2
9	    4,3,2; 6,2,1; 5,1,3
10	    2,3,5; 4,5,1; 6,1,3
10	    2,5,3; 6,3,1; 4,1,5
11	    1,4,6; 3,6,2; 5,2,4
11	    1,6,4; 5,4,2; 3,2,6
12	    1,5,6; 2,6,4; 3,4,5
12	    1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the
maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible
to form 16- and 17-digit strings. What is the maximum 16-digit string
for a "magic" 5-gon ring?
"""

from itertools import permutations

result = 0
# Try to get the first digit as big as possible from the start, i.e. 
# iterate from 6 and down (since the best case is that the outer digits
# are 6, 7, 8, 9, 10).
for outer_0 in range(6, 0, -1):
    for outer_1_to_4 in permutations(range(outer_0+1, 11), 4):
        if 10 not in outer_1_to_4:
            # 10 has to be in the outer ring for the solution string to
            # have length 10
            continue

        outer_ring = (outer_0,) + outer_1_to_4
        for inner_ring in permutations(set(range(1,11)) - set(outer_ring)):
            tripples = [(outer_ring[i], inner_ring[i], inner_ring[(i+1)%5]) for i in range(5)]
            the_sum = sum(tripples[0])
            if any(sum(t) != the_sum for t in tripples):
                # Not magic
                continue

            concat_int = int(''.join(str(x) for t in tripples for x in t))
            result = max(result, concat_int)
    
    if result > 0:
        # All subsequent solutions have smaller first digit, 
        # so we are done
        break

print(result)
correct_answer = "6531031914842725"
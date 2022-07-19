"""
Cubic permutations
The cube, 41063625 ($345^3$), can be permuted to produce two other 
cubes: 56623104 ($384^3$) and 66430125 ($405^3$). In fact, 41063625 is
the smallest cube which has exactly three permutations of its digits
which are also cube.

Find the smallest cube for which exactly five permutations of its
digits are cube.
"""

from itertools import count, takewhile
from collections import Counter, defaultdict


cube_permutations = defaultdict(list)
candidate_keys = set()

previous_length = 1
for i in count():
    n = i**3
    str_n = str(n)
    if len(str_n) > previous_length:
        # Checked all cubes of given length, see if we have an answer
        if candidate_keys:
            result = min(c for k in candidate_keys for c in cube_permutations[k])
            break
        previous_length = len(str_n)
    
    # Use a key that characterizes n up to permutation of the digits. 
    # Here we simply use the sorted digits (as a str).
    k = ''.join(sorted(str_n)) 
    perms_of_n = cube_permutations[k]
    perms_of_n.append(n)

    if len(perms_of_n) == 5:
        candidate_keys.add(k)
    elif len(perms_of_n) > 5:
        candidate_keys.discard(k)

print(result)
correct_answer = "127035954683"
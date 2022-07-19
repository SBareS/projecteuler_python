"""
Prime digit replacements
By replacing the 1st digit of the 2-digit number *3, it turns out that
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all
prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443,
56663, 56773, and 56993. Consequently 56003, being the first member of
this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

from collections import defaultdict
from itertools import combinations
from primes import primes_lt

prime_families = defaultdict(list)
candidate_families = []

def gen_families(p_str : str):
    for c in set(p_str):
        c_inds = [i for i, c1 in enumerate(p_str) if c1 == c]
        # Trick which makes things much faster and simpler: upon 
        # realizing that the number of stars must be a multiple of
        # 3 (since otherwise the family would contain at least one 
        # number that's a multiple of 3), and that this means it will 
        # almost certainly be exactly 3 for the smallest family, we can
        # use itertools.combinations.
        for star_indices in combinations(c_inds, 3):
            chars = list(p_str)
            for i in star_indices:
                chars[i] = '*'
            yield ''.join(chars)

# Guesstimate; big enough to have a prime larger than 10**6. Could also 
# use primes_seq, but that is about 50% slower for this problem.
primes = primes_lt(10**6 + 8)

prev_ndigs = 1
for p in primes:
    p_str = str(p)
    ndigs = len(p_str)
    if ndigs > prev_ndigs:
        if candidate_families:
            # We have a solution!
            break
        prime_families.clear()
        prev_ndigs = ndigs

    for family_str in gen_families(p_str):
        family = prime_families[family_str]
        family.append(p)
        if len(family) >= 8:
            candidate_families.append(family)
else:
    raise Exception("Not enough primes?")

print(min(p for family in candidate_families for p in family))
correct_answer = "121313"
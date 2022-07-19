"""
Digit factorial chains
The number 145 is well known for the property that the sum of the 
factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three
such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually
get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million is
sixty terms.

How many chains, with a starting number below one million, contain
exactly sixty non-repeating terms?
"""

from digits import digits

from math import factorial

N = 10**6

factorials = [factorial(n) for n in range(10)]
def dig_fact_sum(n):
    return sum(factorials[d] for d in digits(n))


chain_elem_bound = 7 * factorial(9) + 1  # 7*9! has 7 digits.
chain_lengths = [0] * chain_elem_bound
for n in range(N):
    if chain_lengths[n]:
        # We've seen n before. Even though we are doing the check below,
        # we need to do this one first to avoid off-by-one errors when
        # (a permutation of) n is part of a loop. Forgetting this 
        # happens to not have any effect on the final result, but we 
        # should keep the check to keep the program formally correct.
        continue
    x = dig_fact_sum(n)
    if chain_lengths[x]:
        # We've seen a permutation of n before, possibly with some 
        # 0/1-digits flipped. This trick captures most numbers, 
        # decreasing the runtime from >1 minute to a few seconds.
        chain_lengths[n] = chain_lengths[x] + 1
        continue

    chain = [n]
    chain_set = {n}
    tail_length = 0
    while x not in chain_set:
        chain_set.add(x)
        if chain_lengths[n]:
            tail_length = chain_lengths[n]
            break
        chain.append(x)
        x = dig_fact_sum(x)
    
    loop = []
    for i, y in enumerate(chain):
        if y == x:
            # Start of loop
            loop = chain[i:]
            break
        chain_lengths[y] = len(chain) - i + tail_length
    loop_set = set(loop)
    for y in loop:
        chain_lengths[y] = len(loop)


print(sum(x == 60 for x in chain_lengths))
correct_answer = "402"
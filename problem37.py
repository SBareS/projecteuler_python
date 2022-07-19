"""
Truncatable primes
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from 
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from itertools import dropwhile
from primes import eratos_lt


prime_bound = 10**6  # Guesstimate
is_prime = eratos_lt(prime_bound)
primes = [p for p in range(prime_bound) if is_prime[p]]

def truncate_right(n):
    return n//10
def truncate_left(n):
    return int(str(n)[1:])

# The problem is a bit simpler if we consider the one-digit primes to be
# truncatable. We will remove them in the end.
left_trunc_primes = {2, 3, 5, 7}
right_trunc_primes = {2, 3, 5, 7}

for p in dropwhile(lambda p: p < 10, primes):
    if truncate_left(p) in left_trunc_primes:
        left_trunc_primes.add(p)
    if truncate_right(p) in right_trunc_primes:
        right_trunc_primes.add(p)

trunc_primes = (left_trunc_primes & right_trunc_primes) - {2, 3, 5, 7}

assert len(trunc_primes) == 11, \
    f"{len(trunc_primes)=}, but expected 11. Need more primes?"

print(sum(trunc_primes))
correct_answer = "748317"
"""
Reversible Prime Squares

Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

    1. It is not a palindrome, and
    2. It is the square of a prime, and
    3. Its reverse is also the square of a prime.

169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares. 
"""

from math import isqrt
from primes import primes_lt

prime_bound = isqrt(10**15) + 1 #Ensures that we get check all prime-squares with <=15 digits

prime_squares = set()
reversible_prime_squares = []
for p in primes_lt(prime_bound):
    psq = p**2
    psq_rev = int(str(psq)[::-1])
    if psq_rev < psq and psq_rev in prime_squares:
        reversible_prime_squares.extend((psq_rev, psq))
    prime_squares.add(psq)
assert len(reversible_prime_squares) >= 50

reversible_prime_squares.sort()
print(sum(reversible_prime_squares[:50]))

correct_answer = "3807504276997394"
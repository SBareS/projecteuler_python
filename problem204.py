"""
Generalised Hamming Numbers
A Hamming number is a positive number which has no prime factor larger
than 5. So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10,
12, 15. There are 1105 Hamming numbers not exceeding $10^8$.

We will call a positive number a generalised Hamming number of type n,
if it has no prime factor larger than n. Hence the Hamming numbers are
the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't
exceed $10^9$?
"""

from primes import primes_lt
from sequences import smooth_numbers

prime_limit = 100
hamming_limit = 10**9
primes = primes_lt(prime_limit + 1)
gen_hamming = smooth_numbers(primes, upper_bound=hamming_limit+1)
print(sum(1 for _ in gen_hamming))
correct_answer = "2944730"
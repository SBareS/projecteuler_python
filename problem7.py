"""
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
see that the 6th prime is 13.

What is the 10 001st prime number?
"""


from itertools import islice
from primes import nth_prime_exact


print(nth_prime_exact(10001))
#print(nth(10001, primes_seq()))
correct_answer = "104743"
"""
5-smooth totients
5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.
Let S(L) be the sum of the numbers n not exceeding L such that Euler's
totient function φ(n) is a Hamming number.
S(100)=3728.

Find $S(10^{12})$. Give your answer modulo $2^{32}$.
"""

from heapq import merge
from itertools import product, takewhile
from primes import is_prime
from sequences import smooth_numbers, squarefree_numbers


N = 10**12
hamming_numbers = list(smooth_numbers([2, 3, 5], upper_bound=N+1))
candidate_primes = [x+1 for x in hamming_numbers if x > 5 and is_prime(x+1)]

result = 0
for sf in squarefree_numbers(candidate_primes, N+1):
    for hn in hamming_numbers:
        if hn * sf > N:
            break
        result += hn * sf
result %= 2**32

print(result)
correct_answer = "939087315"
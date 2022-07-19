"""
Consecutive prime sum
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime 
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
 prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""

from primes import eratos_lt


upper_bound = 10**6
is_prime = eratos_lt(upper_bound)
primes = [p for p in range(upper_bound) if is_prime[p]]

longest_sum = None
longest_sum_length = 0
for i, p in enumerate(primes):
    s = 0
    for j in range(i, len(primes)):
        s += primes[j]
        if s > upper_bound:
            break
        if j - i + 1 > longest_sum_length and is_prime[s]:
            longest_sum = s
            longest_sum_length = j - i + 1

print(longest_sum)
correct_answer = "997651"
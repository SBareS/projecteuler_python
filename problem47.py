"""

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime 
factors each. What is the first of these numbers?
"""

from itertools import count
import factorization
from factorization import prime_power_factors

factorization.generate_default_hints(10**5)  # Guesstimate

def distinct_prime_factors(n):
    return len(prime_power_factors(n))

numbers = count(1)
for n in numbers:
    if (4 == distinct_prime_factors(n) 
        == distinct_prime_factors(next(numbers))
        == distinct_prime_factors(next(numbers))
        == distinct_prime_factors(next(numbers))):
        result = n
        break

print(result)
correct_answer = "134043"
"""
Sum of Squares

Consider equations of the form:
a^2 + b^2 = N, 0 <= a <= b, a, b and N integer.

For N = 65 there are two solutions:
a = 1, b = 8, and a = 4, b = 7.

We call S(N) the sum of the values of a of all solutions of 
a^2 + b^2 = N, 0 <= a <= b, a, b and N integer.

Thus, S(65) = 1 + 4 = 5.

Find the sum of S(N), for all squarefree N only divisible by primes of the 
form 4k + 1 with 4k + 1 < 150.
"""

from primes import primes_lt
from quadratic_integers import prime_sum_of_squares

upper_bound = 150
rational_primes = [p for p in primes_lt(upper_bound) if p % 4 == 1]
gaussian_prime_pairs = []

for p in rational_primes:
    a, b = prime_sum_of_squares(p)
    gaussian_prime_pairs.append(((a, b), (a, -b)))

def rec(i):
    if i == len(gaussian_prime_pairs):
        yield 1, 0
        return
    for a, b in rec(i + 1):
        yield a, b
        for c, d in gaussian_prime_pairs[i]:
            yield a*c - b*d, a*d + b*c

result = sum(min(abs(a), abs(b)) for a, b in rec(0))
result //= 2 #Everything has been counted twice (it and its conjugate)
print(result)

correct_answer = "2032447591196869022"
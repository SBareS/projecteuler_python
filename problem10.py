"""
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from primes import primes_lt


print(sum(primes_lt(2000000)))
correct_answer = "142913828922"
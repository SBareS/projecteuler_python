"""
Sub-string divisibility
The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from digits import digits, undigits


primes = [2, 3, 5, 7, 11, 13, 17]

def all_solutions():
    def rec(previous_two, available, prime_index):
        if prime_index == len(primes):
            yield []
        for d in available:
            digs = previous_two + [d]
            n = undigits(digs)
            if n % primes[prime_index] == 0:
                for tail in rec(digs[1:], available-{d}, prime_index+1):
                    # We return the digits in reverse order, so as to 
                    # avoid quadratic behaviour
                    yield tail + [d]
    
    all_digits = set(range(10))
    for i in range(100, 1000):
        d1, d2, d3 = digits(i)
        dig_set = {d1, d2, d3}
        if len(dig_set) == 3:
            for tail in rec([d2, d3], all_digits - dig_set, 0):
                yield undigits((tail + [d3, d2, d1])[::-1])

print(sum(all_solutions()))
correct_answer = "16695334890"
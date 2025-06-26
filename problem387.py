"""
Harshad Numbers

A Harshad or Niven number is a number that is divisible by the sum of its 
digits. 201 is a Harshad number because it is divisible by 3 (the sum of its 
digits.) When we truncate the last digit from 201, we get 20, which is a 
Harshad number. When we truncate the last digit from 20, we get 2, which is 
also a Harshad number. Let's call a Harshad number that, while recursively 
truncating the last digit, always results in a Harshad number a right 
truncatable Harshad number.

Also: 
201/3 = 67 
which is prime. Let's call a Harshad number that, when divided by the sum of
its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number 
that is also right truncatable. Let's call such primes strong, right 
truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes 
less than 1000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
"""

from digits import digits
from primes import is_prime

# Super easy problem, except for deciphering the problem statement lol.
# Take particular care: "strong, right truncatable Harshad primes" are in fact
# generally *not* Harshad, despite the name.

def is_harshad(n):
    return n % sum(digits(n)) == 0

def trunc_harshads(bound): #Bounded by 10**(bound-1)
    layer = list(range(1, 10))
    yield from layer
    for _ in range(bound-2):
        layer = [10 * n + d 
                 for n in layer for d in range(10) 
                 if is_harshad(10 * n + d)]
        yield from layer

result = 0
for x in trunc_harshads(14):
    if is_prime(x // sum(digits(x))):
        # x is strong trunc Harshad, add primes that truncate to x.
        result += sum(10*x + d for d in range(10) if is_prime(10*x + d))

print(result)

correct_answer = "696067597313468"
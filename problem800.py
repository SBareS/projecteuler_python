"""
Hybrid Integers
An integer of the form $p^q q^p$ with $p\neq q$ prime numbers is
called a hybrid-integer. For example, $800 = 2^5 5^2$ is a 
hybrid-integer.

We define C(n) to be the number of hybrid-integers less than or equal 
to n. You are given $C(800)=2$ and $C(800^{800}) = 10789$ Find 
$C(800800^{800800})$
"""

from itertools import count
from math import ceil, log

from primes import primes_lt


N = 800800
log_bound = N * log(N)
prime_bound = ceil(N * log(N, 2))

primes = primes_lt(prime_bound)

result = 0

j = len(primes)-1
for i in count():
    while primes[i]*log(primes[j]) + primes[j]*log(primes[i]) > log_bound:
        j -= 1
    if j <= i:
        break
    result += j-i

print(result)
correct_answer = "1412403576"
"""
Fibonacci Primitive Roots

When we calculate 8^n modulo 11 for n=0 to 9 we get: 1, 8, 9, 6, 4, 10, 3, 2, 
5, 7.
As we see all possible values from 1 to 10 occur. So 8 is a primitive root of
11.
But there is more:
If we take a closer look we see:
1 + 8 = 9
8 + 9 = 17 \\equiv 6 mod 11
9 + 6 = 15 \\equiv 4 mod 11
6 + 4 = 10
4 + 10 = 14 \\equiv 3 mod 11
10 + 3 = 13 \\equiv 2 mod 11
3 + 2 = 5
2 + 5 = 7
5 + 7 = 12 \\equiv 1 mod 11.
So the powers of 8 mod 11 are cyclic with period 10, and 
8^n + 8^(n+1) = 8^(n+2).
8 is called a Fibonacci primitive root of 11.
Not every prime has a Fibonacci primitive root.
There are 323 primes less than 10 000 with one or more Fibonacci primitive 
roots and the sum of these primes is 1480491.
Find the sum of the primes less than 100 000 000 with at least one Fibonacci 
primitive root. 
"""

# Simply check for each prime if
# 1) there is a root of x^2 - x - 1 modulo p (by quadratic reciprocity, 
# this happens when p is +-1 modulo 5, as well as for p=5); and if
# 2) one of these roots is a primitive root modulo p.

import factorization
from mod_arith import is_primitive_root_modp, sqrt_modp
from primes import is_prime

upper_bound = 100_000_000

# Note: Due to Python's memory overhead, the humble list of integers generated
# below actually takes up several gigabytes of memory. Run this file with 
# caution on shitty laptops...
factorization.generate_default_hints(upper_bound)
primes = (p for p in range(upper_bound + 1) if (p % 5) not in (2, 3) and is_prime(p))

result = 0
for p in primes:
    for sqrt5 in sqrt_modp(5, p):
        phi = (1 + sqrt5) * (p + 1)//2 % p
        if is_primitive_root_modp(phi, p):
            result += p
            break

print(result)
correct_answer = "74204709657207"
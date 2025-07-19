"""
Large Repunit Factors

A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k.

For example, R(10) = 1111111111 = 11 * 41 * 271 * 9091, and the sum of these 
prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9)
"""

from primes import primes_seq

# R(k) = (10^k - 1)//9, which is 0 mod p iff 10^k is 1 mod p. 
# This argument does not work for p = 3 due to the division by 9, but here R(k) 
# is congruent to k mod 3 (in our case k = 10^9 != 0 mod 3).

prime_divs = []
for p in primes_seq():
    if p == 3:
        continue
    if pow(10, 10**9, p) == 1:
        prime_divs.append(p)
        if len(prime_divs) == 40:
            break
print(sum(prime_divs))

correct_answer = "843296"
"""
Spiral primes
Starting with 1 and spiralling anticlockwise in the following way, a 
square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom 
right diagonal, but what is more interesting is that 8 out of the 13 
numbers lying along both diagonals are prime; that is, a ratio of 8/13 
≈ 62%.

If one complete new layer is wrapped around the spiral above, a square 
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of 
primes along both diagonals first falls below 10%?
"""

from itertools import count

from primes import is_prime

prime_count = 0
for n in count(1):
    width = 2*n + 1
    
    # Loop over the corners; the last one is width**2 and they are 
    # width-1 apart. We don't need to include the fourth corner 
    # (width**2), since it cannot be prime.
    for corner in range(width**2 - 3*(width - 1), width**2, width - 1):
        if is_prime(corner):
            prime_count += 1
    if prime_count / (4*n + 1) < 0.1:
        result = width
        break

print(result)
correct_answer = "26241"
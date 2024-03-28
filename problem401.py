"""
Sum of Squares of Divisors
The divisors of 6 are and 1, 2, 3 and 6.
The sum of the squares of these numbers is 1 + 4 + 9 + 36 = 50.

Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6) = 50.
Let SIGMA2(n) represent the summatory function of sigma2(n), that is 
SIGMA2(n) = sigma2(1) + ... + sigma2(n).
The first values of SIGMA2(n) are: 1, 6, 37, 63 and 113. 
Find SIGMA2(10^15) modulo 10^9.
"""

from math import isqrt


themod = 10**9

def sum_of_squares(n):
    return n * (n + 1) * (2*n + 1) // 6 % themod

# By reordering the sum in a clever way, we only have 
# to sum ~sqrt(n) terms to compute SIGMA2(n)
n = 10**15
s = isqrt(n)
result = 0
for k in range(1, s + 1):
    result += sum_of_squares(n // k) + k**2 * (n // k) % themod
    result %= themod
result -= s * sum_of_squares(s) % themod
result %= themod

print(result)
correct_answer = "281632621"
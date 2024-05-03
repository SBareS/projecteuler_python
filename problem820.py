"""
Nth Digit of Reciprocals
Let d_n(x) be the be the nth decimal digit of the fractional part of x, or 0
if the fractional part has fewer than n digits.

For example:
d_7(1) = d_7(1/2) = d_7(1/4) = d_7(1/5) = 0
d_7(1/3) = 3 since 1/3 = 0.3333333333...
d_7(1/6) = 6 since 1/6 = 0.1666666666...
d_7(1/7) = 1 since 1/7 = 0.1428571428...

Let S(n) = d_n(1) + d_n(1/2) + ... + d_n(1/n).

You are given:
S(7) = 0 + 0 + 3 + 0 + 0 + 6 + 1 = 10
S(100) = 417
Find S(107).^
"""

def S(n):
    return sum(pow(10, n, 10*k) // k for k in range(1, n+1))

print(S(10**7))
correct_answer = "44967734"
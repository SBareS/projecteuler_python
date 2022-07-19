"""
Digit fifth powers
Surprisingly there are only three numbers that can be written as the 
sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

from digits import digits

n = 0
while (n + 1) * 9**5 >= 10**n - 1:
    n += 1
upper_bound = (n + 1) * 9**5 # 10**n

def dig_pow5_sum(n):
    return sum(d**5 for d in digits(n))

print(sum (n for n in range(2, upper_bound) if n == dig_pow5_sum(n)))
correct_answer = "443839"
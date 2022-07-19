"""
Powerful digit counts
The 5-digit number, $16807=7^5$, is also a fifth power. Similarly, the
9-digit number, $134217728=8^9$, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


from itertools import count, takewhile
from math import ceil

# a**n has n digits iff
#       10**(n-1)       <= a**n     < 10**n
# <=>   10**((n-1)/n) <= a < 10
# the number of integers a in this interval is
# 10 - ceil(10**((n-1)/n))
# which is decreasing in n and eventually zero.

print(sum(takewhile(lambda x: x, (10 - ceil(10**((n-1)/n)) for n in count(1)))))
correct_answer = "49"
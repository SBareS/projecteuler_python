"""
Champernowne's constant
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of
the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""

from itertools import chain, count, islice

# In principle, d[n] can be computed in O(log(n)) time. This simple 
# solution takes O(n) time to do so, and is thus horribly ineffient. 
# However, since we only need d[10**6], that is no problem.

def champernowne_digits():
    for i in count(1):
        yield from (int(c) for c in str(i))

d = list(chain([0], islice(champernowne_digits(), 10**6)))

result = 1
for n in range(7):
    result *= d[10**n]
print(result)
correct_answer = "210"
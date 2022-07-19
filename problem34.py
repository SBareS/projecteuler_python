"""
Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from itertools import combinations_with_replacement
from math import factorial

from digits import digits

factorials = [factorial(n) for n in range(10)]

# Trick: We don't care about the order of the digits, only the sum of 
# their factorials; i.e. we don't have to check both 145 and 154.
result_numbers = set()
for n_dig in range(2, 8):  # 8 * factorial(9) has less than 8 digits
    for digs in combinations_with_replacement(range(10), n_dig):
        fact_sum = sum(factorials[d] for d in digs)
        fact_sum_digs = digits(fact_sum)
        if tuple(sorted(fact_sum_digs)) == digs:
            result_numbers.add(fact_sum)

print(sum(result_numbers))
correct_answer = "40730"
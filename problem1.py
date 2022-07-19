"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def arithmetic_sequence_sum(first, last, step):
    """Sum of the sequence first, first+step, first+2*step, ..., 
    (last - (last-first)%step)."""
    last -= (last - first)%step
    n_terms = (last - first)//step + 1
    twice_average = first + last
    return n_terms * twice_average // 2

multiples_of_3 = arithmetic_sequence_sum(0, 999, 3)
multiples_of_5 = arithmetic_sequence_sum(0, 999, 5)
multiples_of_15 = arithmetic_sequence_sum(0, 999, 15)

# Inclusion/exclusion
multiples_of_3_or_5 = multiples_of_3 + multiples_of_5 - multiples_of_15

print(multiples_of_3_or_5)
correct_answer = "233168"
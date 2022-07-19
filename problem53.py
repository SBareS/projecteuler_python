"""
Combinatoric selections
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, $\binom{5}{3}=10$.

In general, $\binom{n}{r}=\frac{n!}{r!(n-r)!}$, where $r\le n$, 
$n! = n(n-1)\cdots 1$, and $0! = 1$.

It is not until n=23, that a value exceeds one-million: 
$\binom{23}{10}=11440066$.

How many, not necessarily distinct, values of $\binom{n}{r}$
for $1\le n\le 100$, are greater than one-million?
"""

from itertools import islice


pascal_triangle = [[1]]
for r in range(1, 101):
    previous_row = pascal_triangle[-1] + [0]
    new_row = [1] + [previous_row[i-1] + previous_row[i] for i in range(1, len(previous_row))]
    pascal_triangle.append(new_row)

print(sum(x > 10**6 for row in pascal_triangle for x in row))
correct_answer = "4075"
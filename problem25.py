"""
1000-digit Fibonacci number
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?
"""

from math import ceil, log, sqrt


sqrt5 = sqrt(5)
phi = (1 + sqrt5)/2

# The number of digits in N is ceil(log(N)/log(10)), and 
# Fn = floor(ph**n/sqrt5), so we get the answer by solving
# log(phi**n / sqrt5)/log(10) + 1 >= 1000
# <=> n*log(phi) - log(sqrt5) >= 999*log(10)
# <=> n >= (999*log(10) + log(sqrt5))/log(phi)
# and rounding up.

print(ceil((999*log(10) + log(sqrt5))/log(phi)))
correct_answer = "4782"
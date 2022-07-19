"""
Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are 
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not 
include leading zeros.)
"""

from digits import digits


def base10_palindromes(n_digs):
    if n_digs == 1:
        yield from range(10)
        return
    for i in range(10**(n_digs//2 - 1), 10**(n_digs//2)):
        left = str(i)
        right = left[::-1]
        if n_digs % 2 == 0:
            yield int(left + right)
        else:
            for j in range(10):
                middle = str(j)
                yield int(left + middle + right)

def is_base2_palindrome(n):
    digs = digits(n, 2)
    return digs == digs[::-1]

all_base10_palindromes = (n for ndigs in range(1, 7) for n in base10_palindromes(ndigs))
double_base_palindromes = filter(is_base2_palindrome, all_base10_palindromes)
print(sum(double_base_palindromes))
correct_answer = "872187"
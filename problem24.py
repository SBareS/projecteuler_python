"""
Lexicographic permutations
A permutation is an ordered arrangement of objects. For example, 3124 
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 
3, 4, 5, 6, 7, 8 and 9?
"""

from math import factorial
from digits import factoradic

#TODO: Export this function?
def nth_permutation(n, symbols):
    """Returns the nth permutation (indices starting from 0) on a list 
    (or finite iterable) of symbols. If n > factorial(len(symbols)), 
    the permutations wrap around."""

    # Copy symbols so as to not mess with the original. As a bonus, any
    # finite iterable should now work as input.
    symbols = list(symbols)
    if symbols == []:
        # Special case; the only permutation of the empty list is the 
        # empty list (return early to avoid modding with zero below)
        return []

    n %= factorial(len(symbols))
    n_factoradic = factoradic(n)
    n_factoradic = (len(symbols) - len(n_factoradic))*[0] + n_factoradic

    result = []
    for d in n_factoradic:
        c = symbols[d]
        del symbols[d]
        result.append(c)
    
    return result

print(''.join(map(str, nth_permutation(10**6 - 1, list(range(10))))))
correct_answer = "2783915460"
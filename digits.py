"""Contains functions for extracting digits from a number"""



from itertools import accumulate, count, takewhile
import operator

def digits(n, base=10):
    """Returns a list of the digits of n in the given base (default
     10) in big-endian order."""
    if base == 10:
        # CPython is much faster than I can ever hope to be
        return list(map(int, str(n)))
    if n == 0:
        return [0]
    
    digs_rev = []
    while n > 0:
        n, r = divmod(n, base)
        digs_rev.append(r)
    return digs_rev[::-1]

def undigits(dig, base=10):
    """Returns a number with the digits dig in the given base (default
    10) in big-endigan order."""
    if base == 10:
        # CPython is much faster than I can ever hope to be
        return int(''.join(map(str, dig)))
    
    result = 0
    for d in dig:
        result *= base
        result += d
    return result

def factoradic(n):
    """Returns a list of the digits of n in big-endian factorial 
    base ("factoradic")."""
    factorials = list(takewhile(lambda x: x < n, accumulate(count(1), operator.mul, initial=1)))
    result = []
    for b in factorials[::-1]:
        q, n = divmod(n, b)
        result.append(q)
    return result
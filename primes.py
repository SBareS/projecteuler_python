"""Contains functions for generating and recognizing primes."""

from heapq import heappop, heappush, heappushpop, heapreplace
from itertools import chain, repeat
from math import ceil, floor, log

import factorization
from factorization import extract_factor

# TODO: Hard-coded list of small primes?

def eratos_lt(upper_bound, as_factorization_hints=False):
    """Returns a list, is_prime, of length upper_bound, such that
    is_prime[n] is True if and only if n is prime. Internally uses the
    sieve of Erastostenes.
    
    If as_factorization_hints is set to True, it will in stead generate
    a list factorization_hints where factorization_hint[n] is a prime 
    factor of n and 
    factorization_hint[0] == factorization_hint[1] == None. This can 
    then be used to prime-factorize the numbers less than n much faster
    than by trial division, and it can also still be used to check if n
    is prime, by checking if n == factorization_hint[n]."""
    if as_factorization_hints:
        result = list(range(upper_bound))
        result[2::2] = repeat(2, len(range(2, len(result), 2)))
    else:
        result = [False, True] * ((upper_bound+1) // 2)
        if upper_bound % 2 == 1:
            result.pop()
            # Note: Populating the list with one-too-many elements and then
            # popping is faster than populating the list with one-too-few
            # elements and then appending. This is because CPython knows 
            # exactly how much memory is needed when allocating by [...]*N,
            # so appending afterwards would extend the list.
    
    if as_factorization_hints:
        result[0] = result[1] = None
    else:
        result[1] = False
        result[2] = True

    for p in range(3, upper_bound, 2):
        if p*p > upper_bound:
            break
        if (as_factorization_hints and result[p] != p) or (not result[p]):
            continue
        # Note:
        #   - We only need to sieve odd multiples of p, since the even 
        #   multiples taken care of from the construction of is_prime
        #   - We only need to sieve multiples of p from p*p and up, since 
        #   smaller numbers will have a prime factor smaller than p.
        #   - Doing the hack below is quite a bit faster than the more 
        #   obvious loop-based implementation, simply because CPython
        #   beats out any code you can write by hand...
        result[p*p : upper_bound : 2*p] = repeat(
            p if as_factorization_hints else False,
            len(range(p*p, upper_bound, 2*p)))
        #for np in range(p*p, upper_bound, 2*p):
        #    is_prime[np] = False
    
    return result

def primes_lt(upper_bound):
    """Returns a list of primes less than upper_bound. Internally uses 
    the sive of Erastostenes."""
    is_prime = eratos_lt(upper_bound)
    return [p for p in chain([2], range(3, upper_bound, 2)) if is_prime[p]]

# TODO: Cached version of this. Maybe a cache_seq decorator?
def primes_seq():
    """Iterates over all the primes. Internally uses a heap-based
    priority queue. If you only need primes up to a known bound, using
    primes_lt is probably better. Even if not very sharp, the bounds 
    provided by pi_lower, pi_upper, nth_prime_lower and nth_prime_upper
    will probably give better (i.e. faster) results if fed to primes_lt
    than the result given by this."""
    yield 2
    yield 3
    q = 3
    heap = [(3*3, 3)]
    while True:
        q += 2
        if q != heap[0][0]:
            yield q
            heappush(heap, (q*q, q))
        while q >= heap[0][0]:
            pk, p = heap[0] #heappop(heap)
            heapreplace(heap, (pk + 2 * p, p))  # Sieve odd multiples of p


def pi_exact(x):
    """Exact value of the prime-counting function. Literally computes
    all primes up to x, so very slow."""
    return sum(eratos_lt(floor(x) + 1))

# TODO: Give tighter bounds assuming RH? Alternatively, there are also 
# tighter bounds due to by Dusart.
def pi_lower(x):
    """Returns a proven lower bound for the prime counting function, see
    https://en.wikipedia.org/wiki/Prime-counting_function#Inequalities."""
    if x < 17:
        return 0
    else:
        return ceil(x / log(x))

def pi_upper(x):
    """Returns a proven upper bound for the prime counting function, see
    https://en.wikipedia.org/wiki/Prime-counting_function#Inequalities."""
    # pi(x)*log(x)/x attains its maximum at 113, and pi(113)=30
    K = 30 * log(113) / 113  # approx 1.25506
    floor(K * x / log(x))

def nth_prime_exact(n):
    """Returns the nth prime. This involves calculating the primes up
    to n and a few more, so very slow."""
    return primes_lt(nth_prime_upper(n) + 1)[n-1]

def nth_prime_lower(n):
    """Returns a proven lower bound for the nth prime, see
    https://en.wikipedia.org/wiki/Prime-counting_function#Inequalities."""
    if n == 1:
        return 2
    else:
        return ceil(n * (log(n * log(n)) - 1))

def nth_prime_upper(n):
    """Returns a proven upper bound for the nth prime, see
    https://en.wikipedia.org/wiki/Prime-counting_function#Inequalities."""
    if n < 6:
        return 11  # 5th prime
    else:
        return floor(n * log(n * log(n)))

def miller_rabin(n, a):
    """Runs the Miller-Rabin probable-prime test on n with witness a. 
    If n is prime, this will always return True. If n is not prime, 
    there will be at most n/4 possible values of a among 1,...,n-1 
    for which True is returned (see Rabin, Michael O. (1980), 
    "Probabilistic algorithm for testing primality"). Therefore, running
    this test for N random values of a gives at most 1/4^N chance of a 
    false positive."""
    s, d = extract_factor(n-1, 2)  # n = 2^s*d with d odd
    a = pow(a, d, n)
    if a == 1 or a == n-1:
        return True
    for _ in range(s):
        a = (a*a) % n  # a**(2**i * d)
        if a == 1:
            # Found a square-root of 1 that is not +-1, thus Z/nZ is 
            # not a field, thus n is definitely not prime
            return False  
        if a == n-1:
            return True
    # Either we have a**(n-1) not congruent to 1, contradicting 
    # Fermat's Little Theorem, or it is congruent to 1, in which case 
    # we have a square root of one that is not +-1. In either case, n
    # cannot be prime.
    return False

_small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
def is_prime(n):
    """Returns True if n is a (probable) prime and False if n is 
    composite. Internally uses a probabilistic test (Miller-Rabin), so
    there is a very small chance of false positives; but the output is
    guaranteed to be correct for n < 2**64. If prime hints have been generated
    in the factorization module, those will be used when n is small enough."""
    if n < len(factorization.default_hints):
        return factorization.default_hints[n] == n
    if n <= _small_primes[-1]:
        return n in _small_primes
    return all(miller_rabin(n, a) for a in _small_primes)

def merge_prime_powers(pp1, pp2):
    """
    Given prime factorizations of two integers (as sorted lists of prime-power
    pairs (p, k)), returns the prime factorization of their product.
    """
    result = []
    i = j = 0
    while i < len(pp1) and j < len(pp2):
        p1, k1 = pp1[i]
        p2, k2 = pp2[j]
        if p1 < p2:
            result.append((p1, k1))
            i += 1
        elif p1 > p2:
            result.append((p2, k2))
            j += 1
        else:
            result.append((p1, k1 + k2))
            i += 1
            j += 1
    result.extend(pp1[i:])
    result.extend(pp2[j:])
    return result
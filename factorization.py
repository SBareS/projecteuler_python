"""Contains methods for factoring numbers into primes."""

from collections import defaultdict
from functools import wraps
from itertools import product
from math import isqrt, prod

class FactorizationError(Exception):
    pass

default_primes = []
"""Assign a list of primes to this variable to use by default. In most
situations, it makes more sense to call generate_default_primes 
than to assign this directly."""

default_hints = []
"""Assign a list of prime factor hints to this variable to use by 
default. In most situations, it makes more sense to call 
generate_default_hints than to assign this directly."""

def generate_default_primes(limit):
    """Sets default_primes to primes.primes_lt(limit)"""
    from primes import primes_lt
    global default_primes
    if default_primes and default_primes[-1] >= limit:
        return
    default_primes = primes_lt(limit)

def generate_default_hints(limit):
    """Sets default_hits to 
    primes.eratos_lt(limit, as_factorization_hints=True)"""
    from primes import eratos_lt
    global default_hints
    if len(default_hints) > limit:
        return
    default_hints = eratos_lt(limit, as_factorization_hints=True)

def generate_default_primes_and_hints(limit):
    """Simultaneously generate default primes and default hints. Faster 
    than calling generate_default_primes and generate_default_hints 
    separately."""
    global default_primes
    generate_default_hints(limit)
    if default_primes and default_primes[-1] >= limit:
        return
    default_primes = [p for n, p in enumerate(default_hints) if n == p]

def _use_default_primes(f):
    @wraps(f)
    def wrapper(*args, primes=None, **kwargs):
        if primes is None:
            primes = default_primes
        return f(*args, primes=primes, **kwargs)
    return wrapper

def _use_default_hints(f):
    @wraps(f)
    def wrapper(*args, hints=None, **kwargs):
        if hints is None:
            hints = default_hints
        return f(*args, hints=default_hints, **kwargs)
    return wrapper

@_use_default_hints
@_use_default_primes
def prime_power_factors(n, *, primes, hints):
    """Returns a list [(p1, k1), ..., (pr, kr)] such that 
    n = p1**k1 * ... * pr**kr, where p1 < ... < pr are primes and 
    k1, ..., kr are positive integers."""
    if n <= 0:
        raise ValueError("Can only factor positive integers.")
    if n == 1:
        return []
    
    power_of = defaultdict(int)
    
    # Do trial division until we can use the hints.
    for p in primes:
        if p*p > n or n < len(hints):
            break
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k > 0:
            power_of[p] = k
    
    while 1 < n < len(hints):
        # Now that we have hints, we can go fast
        p = hints[n]
        power_of[p] += 1
        n //= p
    
    if n > 1:
        if primes and primes[-1]**2 > n:
            # No worries, we simply have one prime factor left
            power_of[n] += 1
        else:
            # Uh-oh, seems the factorization failed
            raise FactorizationError(
                (f"Not enoguh primes/hints. We need primes up to " 
                f"{isqrt(n)+1} or hints up to {n}."))
    
    return sorted(power_of.items())

@_use_default_hints
@_use_default_primes
def prime_factors(n, *, primes, hints):
    """Returns a list [p1, ..., pr] of all the prime factors of n (with 
    multiplicities), such that n = p1 * ... * pr and p1 <= ... <= pr."""
    return [p for p, k in prime_power_factors(n, primes=primes, hints=hints) for _ in range(k)]

@_use_default_hints
@_use_default_primes
def unique_prime_factors(n, *, primes, hints):
    """Returns a list [p1, ..., pr] of the unique prime factors of n, 
    such that p1 < ... < pr."""
    return [p for p, k in prime_power_factors(n, primes=primes, hints=hints)]

def extract_factor(n, d):
    """Returns (k, u) such that n = d^k*u, and d does not divide u."""
    k, u = 0, n
    while u % d == 0:
        u //= d
        k += 1
    return k, u

@_use_default_hints
@_use_default_primes
def divisors(n, *, primes, hints):
    """Returns a list of the divisors of n in increasing order."""
    if n == 1:
        return [1]
    ps, ks = zip(*prime_power_factors(n, primes=primes, hints=hints))
    pps = []
    for p, k in zip (ps, ks):
        pp = []
        q = 1
        for r in range(k+1):
            pp.append(q)
            q *= p
        pps.append(pp)
    result = [prod(qs) for qs in product(*pps)]
    result.sort()
    return result
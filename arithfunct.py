"""Contains functions relating to multiplicative and additive functions
A function f : N -> C is called multiplicative if for any n, m with 
gcd(n, m) = 1 we have f(n*m) = f(n) * f(m). In particular, such a
function is determined by its values on prime powers, since
f(p1**k1 * p2**k2 * ... * pr**kr) 
    = f(p1**k1) * f(p2**k2) * ... * f(pr**kr).
Similarly, f is called additive if for n, m with gcd(n, m) we have
f(n*m) = f(n) + f(m), in which case
f(p1**k1 * p2**k2 * ... * pr**kr) 
    = f(p1**k1) + f(p2**k2) + ... + f(pr**kr).
    
Several functions in this module have a _pp-version (i.e. sigma_nat_pp)
which takes a tuple (p,k) as the argument and computes the corresponding
multiplicative/additive function for the prime power p**k."""

from functools import wraps
from itertools import count
from math import prod

from factorization import prime_power_factors
from primes import primes_lt

def multfunct_from_pp(f):
    """Given a function taking a tuple (p, k), interpreted as a prime 
    power, returns the corresponding multiplicative function. Can be 
    used as a decorator."""
    @wraps(f)
    def wrapper(n):
        return prod(map(f, prime_power_factors(n)))
    return wrapper

def addfunct_from_pp(f):
    """Given a function taking a tuple (p, k), interpreted as a prime 
    power, returns the corresponding additive function. Can be 
    used as a decorator."""
    @wraps(f)
    def wrapper(n):
        return sum(map(f, prime_power_factors(n)))
    return wrapper

def multfunc_table(f, upper_bound, primes=None):
    """Given a function f taking a tuple (p, k), computes list tab of 
    length upper_bound containing the value of the corresponding
    multiplicative function. Can optionally be given a list of primes
    less than upper_bound, otherwise these are computed first."""
    if primes == None:
        primes = primes_lt(upper_bound)
    result = upper_bound*[1]
    result[0] = 0

    for p in primes:
        p_pow_k = p
        for k in count(1):
            f_pk = f((p, k))
            # NB: Skipping f_pk == 1 can improve performance by a quite 
            # a bit for some functions (eg. euler_phi((2,1)) == 1).
            if f_pk != 1:
                for u in range(1, (upper_bound-1)//p_pow_k + 1):
                    if u%p != 0:
                        result[u*p_pow_k] *= f_pk
            
            p_pow_k *= p
            if p_pow_k >= upper_bound:
                break
    return result

def sigma_nat_pp(pk, a=1):
    p, k = pk
    return (p**((k + 1)*a) - 1)//(p**a - 1) if a else k + 1
def sigma_nat(n, a=1):
    """Sum of the ath powers of the divisors of n. By default, a=1, 
    i.e., sigma(n) is the sum of the divisors of n. Another important 
    special case is a=0, which counts the number of divisors of n. This
    version assumes a is a non-negative integer and returns an integer;
    for a general version see sigma_gen."""
    return prod(sigma_nat_pp(pk, a=a) for pk in prime_power_factors(n))

def sigma_gen_pp(pk, a=1):
    p, k = pk
    return (p**((k + 1)*a) - 1)/(p**a - 1) if a else k + 1
def sigma_gen(n, a=1):
    """Sum of the ath powers of the divisors of n. By default, a=1, 
    i.e., sigma(n) is the sum of the divisors of n. Another important 
    special case is a=0, which counts the number of divisors of n. This
    version does not return an integer. For a version that returns an 
    integer (assuming a is a non-negative integer), see sigma_nat."""
    return prod(sigma_gen_pp(pk, a=a) for pk in prime_power_factors(n))

def euler_phi_pp(pk):
    p, k = pk
    return p**(k-1) * (p - 1)
def euler_phi(n):
    """Euler's phi function."""
    return prod(map(euler_phi_pp, prime_power_factors(n)))

def mobius_pp(pk):
    p, k = pk
    return -1 if k == 1 else 0
def mobius(n):
    """The mobius function."""
    return prod(map(mobius_pp, prime_power_factors(n)))
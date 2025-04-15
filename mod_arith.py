"""Contains some helper functions for modular arithmetic. Also contains 
a class for numbers mod m which inherits from int."""

from functools import cache, reduce
from itertools import zip_longest
from digits import digits
from math import comb, prod

from factorization import extract_factor

def xgcd(x, y):
    """Returns a tripple (g, s, t) where g = gcd(x, y), and s, t 
    satisfy Bezout's identity x*s + y*t == g."""
    s1, t1 = 1, 0
    s2, t2 = 0, 1
    while y != 0:
        # Invariant: s1 * x0 + t1 * y0 = x, s2 * x0 + t2 * y0 = y, 
        # where x0, y0 are the initial x, y.
        q, r = divmod(x, y)
        x, y, s1, t1, s2, t2 = y, r, s2, t2, s1 - q*s2, t1 - q*t2
    return (x, s1, t1)

# DEPRECATED: Use pow(x, -1, m) instead
#def modinv(m, x):
#    """Computes the inverse of x modulo m, assuming x and m are coprime"""
#    return pow(x, -1, m)
#    g, s, t = xgcd(m, x)
#    assert g == 1, "m and x should be coprime"
#    return t

# DEPRECATED: Use pow(x, p-2, p) instead
#def modinv_prime(p, x):
#    """Computes the inverse of x modulo p, assuming p is prime and that
#    p does not divide x. This will usually be quite a bit faster than 
#    modinv(p, x)"""
#    return pow(x, p-2, p)

def inverse_table(p, N):
    """Computes a table of the inverses of 1,...,N modulo p (with None
    on the 0th entry). Can be much faster than calling pow(x, -1, p) N
    times. If N is set to None, computes a table of all inverses mod p."""
    invs = (N+1)*[1]
    invs[0] = None
    for x in range(2, N+1):
        invs[x] = p - (p//x * invs[p%x] % p)
    return invs

def crt2(t1, t2):
    """Given two tuples (m1, a1) and (m2, a2) with m1 and m2 relatively
    prime, computes 0 <= x < m1*m2 such that x is congruent to ai modulo
    mi for i=1,2."""
    m1, a1 = t1
    m2, a2 = t2
    #g, s, t = xgcd(m1, m2)
    #if g != 1:
    #    raise ValueError(f"{m1} and {m2} are not relatively prime.")
    #return (a1 * t * m2 + a2 * s * m1) % (m1 * m2)
    # Using python's builtin modular inverse is quite a bit faster than xgcd
    return (a1 * pow(m2, -1, m1) * m2 + a2 * pow(m1, -1, m2) * m1) % (m1 * m2)

def orth_idemp(L):
    """Given a list of pairwise coprime numbers [m1, ..., mn], computes a list
    of orthogonal idempotents [e1, ..., en] modulo m1*...*mn such that 
    ei % mj is 1 if i == j and 0 otherwise. The map 
    (x1, ..., xn) |-> x1*e1 + ... + xn*en
    thus gives an explicit isomorphism between Z/(m1) x ... x Z/(mn) and
    Z/(m1*...*mn)."""
    m = prod(L)
    return [pow(m // n, -1, n) * (m // n) for n in L]

# def _crt_folder(t1, t2):
#     return (t1[0]*t2[0], crt2(t1, t2))

def crt(L):
    """Given a list of tuples (mi, ai) with all the m's pairwise 
    relatively prime, computes 0 <= x < a0 * a1 * .. * an, such 
    that, x is congruent to ai mod mi for each i."""
    # m, x = reduce(_crt_folder, L)
    # return x
    es = orth_idemp([t[0] for t in L])
    return sum(e * t[1] for (e, t) in zip(es, L)) % prod(t[0] for t in L)

def binom_modp(n, k, p):
    """Efficiently computes the binomial coefficient n-choose-k modulo
    a prime p using Lucas' theorem."""
    if n < 0:
        raise ValueError("Negative upper indices not supported")
    if not (0 <= k <= n):
        return 0
    
    n_digs = digits(n, p)[::-1]
    k_digs = digits(k, p)[::-1]
    result = 1
    #for ni, ki in zip_longest(n_digs, k_digs, fillvalue=0):
    # We don't have to zip_longest, since the filled ki=0 give binomial 
    # coefficients equal to 1.
    for ni, ki in zip(n_digs, k_digs):
        result *= comb(ni, ki) % p
        result %= p
        if result == 0:
            break
    return result

def legendre_symbol(x, p):
    """The legendre symbol (x/p), equal to +1 when x is a quadratic 
    residue modulo the odd prime p, -1 if it is a nonresidue and 0 if x is zero
    modulo p."""
    y = pow(x, (p-1)//2, p)
    return y if y <= 1 else y - p

def quadratic_nonresidue_modp(p):
    """Returns a quadratic nonresidue modulo p"""
    return filter(lambda x: legendre_symbol(x, p) == -1, range(2, p)).__next__()

def sqrt_modp(x, p):
    """Computes the square roots of x modulo the prime p as a list. Note this
    list will be empty if x is not a quadratic residue modulo p."""
    if p == 2:
        return [x % p]
    if p % 4 == 3:
        y = pow(x, (p+1)//4, p)
    else: # p % 4 == 1, use Tonelli-Shanks 
        s, q = extract_factor(p-1, 2) # p-1 = 2^s * q
        z = quadratic_nonresidue_modp(p)
        (m, c, t, r) = (s, pow(z, q, p), pow(x, q, p), pow(x, (q+1)//2, p))
        while t > 1:
            tt = pow(t, 2, p)
            i = 1
            while tt != 1:
                tt = pow(tt, 2, p)
                i += 1
            b = c
            for _ in range(m - i - 1):
                b = pow(b, 2, p)
            (m, c) = (i, pow(b, 2, p))
            (t, r) = (t*c % p, r*b % p)
        if t == 0:
            y = 0
        else: # t == 1
            y = r
    
    if (y**2 - x) % p != 0:
        return []
    elif y == 0:
        return [0]
    else:
        return sorted([y, p-y])
    
# TODO: sqrt mod p
# TODO: hensel-lifting

@cache
def ZMod(m) -> type:
    """Type of integers modulo m. Note: Even though the type in question
    inherits from int, it performs quite poorly compared to manually 
    modding when needed, since each calculation involves calling a few
    functions in order to create the object."""
    class ZModm(int):
        def __new__(cls, x):
            return int.__new__(cls, x % m)
        # NB: in all the below, we call int.foo(self, ...) directly 
        # instead of super().foo(...), so as to avoid the additional
        # overhead associated with super().
        def __add__(self, other):
            return ZModm(int.__add__(self, other))
        def __radd__(self, other):
            return ZModm(int.__radd__(self, other))
        def __sub__(self, other):
            return ZModm(int.__sub__(self, other))
        def __rsub__(self, other):
            return ZModm(int.__rsub__(self, other))
        def __mul__(self, other):
            return ZModm(int.__mul__(self, other))
        def __rmul__(self, other):
            return ZModm(int.__rmul__(self, other))
        def __pow__(self, n):
            return ZModm(int.__pow__(self, n, m))
        def __truediv__(self, other):
            return self * pow(other, -1, m)
        def __rtruediv__(self, other):
            return pow(self, -1, m) * other
    
    ZModm.__name__ = f"ZMod({m})"
    ZModm.__qualname__ = ''.join([*ZModm.__qualname__.split('.')[:-3], f'ZMod({m})'])
    return ZModm
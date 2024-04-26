"""
Chinese Leftovers

Let g(a, n, b, m) be the smallest non-negative solution to the system:
x = a mod n
x = b mod m
if such a solution exists, otherwise 0.

E.g. g(2, 4, 4, 6) = 10, but g(3, 4, 4, 6) = 0.

Let phi(n) be Euler's totient function.

Let f(n, m) = g(phi(n), n, phi(m), m)
Find the sum of f(n, m) for 1000000 <= n < m < 1005000. 
"""


from math import gcd
from arithfunct import euler_phi_pp, multfunc_table

lower_bound = 1_000_000
upper_bound = 1_005_000

phi_tab = multfunc_table(euler_phi_pp, upper_bound)

#def g(a, n, b, m):
#    d, s, t = xgcd(n, m)
#    if (a - b) % d != 0:
#        return 0
#    return (a * t * m + b * s * n) // d % (m * n // d)

def f(n, m):
    # One could calculate this directly using CRT. However, baiguzair from the
    # forums has given an explicit formula which is in practice much faster,
    # as we can delegate the modular inverse to the builtin pow(x, -1, M)
    # instead of calculating xgcd ourselves.
    d = gcd(n, m)
    if (phi_tab[m] - phi_tab[n]) % d != 0:
        return 0
    return (n * (pow(n // d, -1, m//d) * (phi_tab[m] - phi_tab[n]) // d % (m // d)) + phi_tab[n])
    # return g(phi_tab[n], n, phi_tab[m], m)

print(sum(f(n, m) for n in range(lower_bound, upper_bound) for m in range(n+1, upper_bound)))
correct_answer = "4515432351156203105"
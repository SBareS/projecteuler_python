"""
Best Approximations
Let x be a real number.
A best approximation to x for the denominator bound d is a rational number r/s
in reduced form, with s <= d, such that any rational number which is closer 
to x than r/s has a denominator larger than d:

|p/q - x| < |r/s - x|    ->    q > d

For example, the best approximation to sqrt(13) for the denominator bound 20 
is 18/2 and the best approximation to sqrt(13) for the denominator bound 30 is
101/28.

Find the sum of all denominators of the best approximations to sqrt(n) for the
denominator bound 10^12, where n is not a perfect square and 1 <= n <= 100000. 
"""

from decimal import Decimal, localcontext
from math import isqrt
from cfrac import convergents, sqrt_cfrac

# gives the (weak) best approximation of sqrt(n) with denominator <= d 
# as (numerator, denominator)-pair. Assumes n is not square
def best_appr_of_sqrt(n, d):
    b = None
    for (p, q) in convergents(sqrt_cfrac(n)):
        if q > d:
            break
        a = b
        b = (p, q)
    
    p0, q0 = a
    p1, q1 = b # strong best approximation with denominator bound d
    r = (d - q0)//q1
    p2, q2 = p0 + r*p1, q0 + r*q1 # Candidate semiconvergent
    
    # p1/q1 is a *very* good approximation to sqrt(n): The error is less than
    # 1/q1**2 ~ 10**(-24), and may sometimes be significantly smaller still 
    # (if the partial quotients are large). Thus, to be able to tell whether 
    # p2/q2 is a better approximation, we will will need a lot of numerical 
    # precission
    with localcontext() as ctx:
        ctx.prec = 80
        diff1 = abs(Decimal(n).sqrt() - Decimal(p1)/Decimal(q1))
        diff2 = abs(Decimal(n).sqrt() - Decimal(p2)/Decimal(q2))
        
        return (p1, q1) if diff1 < diff2 else (p2, q2)

def is_square(n):
    return isqrt(n)**2 == n

print(sum(best_appr_of_sqrt(n, 10**12)[1] for n in range(1, 100001) if not is_square(n)))
correct_answer = "57060635927998347"
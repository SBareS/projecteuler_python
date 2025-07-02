"""
Problem 18i

Let R(p) be the remainder when the product from 0 to p-1 of (x^3 - 3x + 4) is 
divided by p. For example R(11) = 0, and R(29) = 13.

Find the sum of R(p) over all primes p between and 1000000000 and 1100000000.
"""


from mod_arith import sqrt_modp
from primes import is_prime


lower_bound = 1_000_000_000
upper_bound = 1_100_000_000

# Way to nerd-snipe a Galois theory enthusiast, lol.
# 
# Hint is in the title: The discriminant of x^3 - 3x + 4 is -324 = -18^2.
# Primes where the polynomial has a root can obviously be skipped. If it 
# doesn't have a root, let x1, x2, x3 be the roots in the splitting field.
# Then the product of interest is
# prod((x - x1) * (x - x2) * (x - x3) for x in Fp)
# = -(x1**p - x1) * (x2**p - x2) * (x3**p - x3)                 (*)
# where we used X**P - X = prod(X - x for x in Fp) evaluated at X=xi. As the 
# Frobenius map permutes the roots, this equals
# plus or minus (x1 - x2) * (x2 - x3) * (x3 - x1),              (**)
# so the product (when it is nonzero) is one of the two square-roots of the
# discriminant. Further, if -324 is not a square mod p (<=> p = 4k + 3) the 
# above frobenius trick must fail, which must be because there was already a 
# root in Fp.
# 
# This leaves only cases when p = 1 mod 4. In this case, we calculate the 
# product as the square root of -324. We still need to pick the right one of
# the two square roots, though. For this we split up according to p mod 3.

result = 0

# If p = 3k + 1 (=> 1 mod 12), then 3 is a square modulo p, so -2 +- sqrt(3)
# live in Fp. The roots are S + T where S, T are appropriate cube roots of 
# -2 +- sqrt(3) satisfying ST = 1 and S^3 + T^3 = -4. Then 
# (S^3)^(3k) = (S^3)^(p-1) = 1 by FLT, so
# w := S^(p-1) = (-2 + sqrt(3))^k is a 3rd root of unity.
# Then, as S^p = wS, (*) becomes 
# R(p) = -(wS + w^2T - S - T)(w^2S + wT - wS + w^2T)(S + T - w^2S - wT) 
#      = -6 * sqrt(3) * w * (1 - w)
# Where the sqrt(3) is the one same as used in w. 

for p in range(lower_bound + (1 - lower_bound)%12, upper_bound, 12):
    if not is_prime(p):
        continue
    sqrt3 = sqrt_modp(3, p)[0]
    omega = pow(-2 + sqrt3, (p-1)//3, p)
    result += -6 * sqrt3 * omega * (1 - omega) % p

# If p = 3k + 1 (=> 5 mod 12), then -2 +- sqrt(3) instead live in F_p^2. 
# We then get a 3rd root of unity
# w := (-2 + sqrt(3))^(k+1)
# with S^p = wT. This flips the sign on the permutation in (**), giving
# R(p) = +6 * sqrt(3) * w * (1 - w).
# The computation has to be carried out in Fp(sqrt(3)), but on the other hand
# we don't need to run Tonelli-Shanks; so it ends up being only a bit slower 
# than the 3k + 1 case. 
for p in range(lower_bound + (5 - lower_bound)%12, upper_bound, 12):
    if not is_prime(p):
        continue
    pwx, pwy = -2, 1
    omx, omy = 1, 0
    k = (p + 1)//3
    while k:
        k, r = divmod(k, 2)
        if r:
            omx, omy = (pwx*omx + 3*pwy*omy) % p, (pwx*omy + pwy*omx) % p
        pwx, pwy = (pwx*pwx + 3*pwy*pwy) % p, 2*pwx*pwy % p
    result += 18 * omy * (1 - 2 * omx) % p

print(result)

correct_answer = "842507000531275"
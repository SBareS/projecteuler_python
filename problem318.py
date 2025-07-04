
"""
2011 Nines

Consider the real number sqrt(2) + sqrt(3).
When we calculate the even powers of sqrt(2) + sqrt(3) we get:
(sqrt(2) + sqrt(3))^2 = 9.898979485566356...
(sqrt(2) + sqrt(3))^4 = 97.98979485566353...
(sqrt(2) + sqrt(3))^6 = 969.998969071069263...
(sqrt(2) + sqrt(3))^8 = 9601.999895855029907...
(sqrt(2) + sqrt(3))^10 = 95049.999989479221...
(sqrt(2) + sqrt(3))^12 = 940897.9999989371855...
(sqrt(2) + sqrt(3))^14 = 9313929.99999989263...
(sqrt(2) + sqrt(3))^16 = 92198401.99999998915...

It looks as if the number of consecutive nines at the beginning of the 
fractional part of these powers is non-decreasing. In fact it can be proven 
that the fractional part of (sqrt(2) + sqrt(3))^2n approaches 1 for large n.

Consider all real numbers of the form sqrt(p) + sqrt(q) with p and q positive 
integers and p < q, such that the fractional part of (sqrt(p) + sqrt(q))^2n
approaches 1 for large n.

Let C(p, q, n) be the number of consecutive nines at the beginning of the 
fractional part of (sqrt(p) + sqrt(q))^2n.

Let N(p, q) be the minimal value of n such that C(p, q, n) >= 2011.

Find the sum of N(p, q) for p + q <= 2011. 
"""

# Simply look for p, q where (sqrt(p) + sqrt(q))^2 = p + q + 2*sqrt(pq) is a
# Pisot number, i.e. where its conjugate p + q - 2*sqrt(pq) is less than 1
# (note both are guaranteed to be positive, as they are squares). For these 
# numbers, as the fractional part of (p + q + 2*sqrt(pq))^2n is 
# 1 - (p + q - 2*sqrt(pq))^2n, we simply have to log(10^-2011) to the base of
# the conjugate.

from math import ceil, log10, sqrt

result = 0
for p in range(1, 2011//2 + 1):
    for q in range(p+1, 2011-p + 1):
        t = p + q - 2*sqrt(p*q)
        if 0 < t < 1:
            result += ceil(-2011/log10(t))
        else:
            break

print(result)

correct_answer = "709313889"
"""
Strong Repunits
The number 7 is special, because 7 is 111 written in base 2, and 11 
written in base 6 (i.e. $7_{10} = 11_6 = 111_2$). In other words, 7
is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit. It
can be verified that there are 8 strong repunits below 50: 
{1,7,13,15,21,31,40,43}. Furthermore, the sum of all strong repunits 
below 1000 equals 15864. Find the sum of all strong repunits below 
$10^{12}$. 
"""

from math import isqrt

# Any number n>2 is a repunit in base n-1, so any repunit with >=3
# digits will be a strong repunit.
N = 10**12
strong_repunits = {1}

for b in range(2, isqrt(N)+1):
    repunit = b + 1
    while (repunit := b * repunit + 1) < N:
        strong_repunits.add(repunit)

print(sum(strong_repunits))
correct_answer = "336108797689259276"
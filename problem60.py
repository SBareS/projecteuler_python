"""
Prime Pair Sets

Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For 
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this 
property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""

# Simple brute-force. Checking primes < 10_000 turns out to be sufficient,
# which is convenient, as we then only have to use a sieve up to 99999999
# (if it were <= 10_000 we would need a sieve up to 1000010000 = 
# 10**9 + 10**4, which is obviously too much, so we would have had to resort 
# to Miller-Rabin).

from math import floor, log10
from primes import eratos_lt

prime_bound = 9_999
sieve_bound = 9_999_9_999
prime_tab = eratos_lt(sieve_bound)
primes_to_bound = [p for p in range(prime_bound) if prime_tab[p]]
n_primes = len(primes_to_bound)

def check(p, q):
    dp = floor(log10(p)) + 1
    dq = floor(log10(q)) + 1
    return prime_tab[10**dq * p + q] and prime_tab[10**dp * q + p]

quints = []
for i1 in range(n_primes):
    p1 = primes_to_bound[i1]
    for i2 in range(i1 + 1, n_primes):
        p2 = primes_to_bound[i2]
        if not check(p1, p2):
            continue
        for i3 in range(i2 + 1, n_primes):
            p3 = primes_to_bound[i3]
            if not all(check(p, p3) for p in (p1, p2)):
                continue
            for i4 in range(i3 + 1, n_primes):
                p4 = primes_to_bound[i4]
                if not all(check(p, p4) for p in (p1, p2, p3)):
                    continue
                for i5 in range(i4 + 1, n_primes):
                    p5 = primes_to_bound[i5]
                    if all(check(p, p5) for p in (p1, p2, p3, p4)):
                        quints.append([p1, p2, p3, p4, p5])

print(min(sum(s) for s in quints))

correct_answer = "26033"
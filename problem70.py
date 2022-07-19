"""
Totient permutation
Euler's Totient function, φ(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive 
number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a 
permutation of 79180.

Find the value of n, $1 < n < 10^7$, for which φ(n) is a permutation of
n and the ratio n/φ(n) produces a minimum.
"""

from math import inf, sqrt, isqrt
from itertools import dropwhile, takewhile
from primes import primes_lt

## Slow, but provably correct-and-halting solution
#N = 10**7
#phi_table = multfunc_table(euler_phi_pp, N+1)
#
#result = None
#min_n_over_phin = inf
#for n in range(2, N+1):
#    phin = phi_table[n]
#    if n/phin < min_n_over_phin and sorted(str(n)) == sorted(str(phin)):
#        result = n
#        min_n_over_phin = n/phin

# Heuristic solution, which is provably correct, but might not give an 
# answer: Look for the answer among products of two large primes (Note:
# p-1 cannot be a digit-permutation of p, so single primes don't work).
# With some careful estimates, one can prove that there are no solutions 
# that are products of three or more primes. The original "proof" on the
# forum is not at all satisfactory, though. However pjhuxford points out
# (as the first person in 15 years...) the lower bound 
# 1/((1-N**(-1/3))*(1-N**(-2/3))) for phi(n) if n<=N has at least three
# prime factors. Thus, if phi(result) is less than this, we have a 
# provably correct result. 
# 
# As an additional heuristic optimization, we need only look for the two
# primes in an interval [sqrt(N)/a, sqrt(N)*a], as long as we check 
# afterwards that our solution's phi-value is less than 
# 1/(1-a/(sqrt(N))). 
# 
# Of course, by falling back to the previous algorithm in case of 
# failure, and/or dynamically increasing the bounds on a and the number
# of prime factors, this can in principle be turne into a 
# provably-halting provably-correct *and* fast algorithm; but since it 
# does give us an answer with the sensibly-guesstimated parameter a=3, I
# just can't be bothered.

N = 10**7
a = 3
primes = list(dropwhile(lambda x: x**2 < N//a, primes_lt(a * isqrt(N))))

result = None
min_n_over_phin = inf
for p in primes:
    for q in takewhile(lambda x: x <= p and p*x <= N, primes):
        n = p*q
        phin = (p - 1)*(q - 1) if p != q else p*(p-1)
        if n / phin < min_n_over_phin and sorted(str(n)) == sorted(str(phin)):
            result = n
            min_n_over_phin = n / phin

# Prove that our solution is correct
assert result, "No solution candidate found :-("
assert min_n_over_phin < 1/(1-a/(sqrt(N))), \
    f"Cannot prove that there are no solutions with primes outside [{sqrt(N)/a}, {sqrt(N)*a}]"
assert min_n_over_phin < 1/((1-N**(-1/3))*(1-N**(-2/3))), \
    "Cannot that the solution is not a product of three primes :-("

# yay!
print(result)
correct_answer = "8319823"
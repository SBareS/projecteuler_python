"""
Riffle Shuffles
A riffle shuffle is executed as follows: a deck of cards is split into two 
equal halves, with the top half taken in the left hand and the bottom half
taken in the right hand. Next, the cards are interleaved exactly, with the top
card in the right half inserted just after the top card in the left half, the
2nd card in the right half just after the 2nd card in the left half, etc.
(Note that this process preserves the location of the top and bottom card of
the deck)

Let s(n) be the minimum number of consecutive riffle shuffles needed to
restore a deck of size n to its original configuration, where n is a positive
even number.

Amazingly, a standard deck of 52 cards will first return to its original 
configuration after only 8 perfect shuffles, so s(52) = 8. It can be verified
that a deck of 86 cards will also return to its original configuration after
exactly  8 shuffles, and the sum of all values of that satisfy is s(n) = 8 is
412.

Find the sum of all values of n that satisfy s(n) = 60.
"""


from math import prod
import factorization

from arithfunct import sigma_nat_pp
from factorization import prime_factors, prime_power_factors

# The order of the riffle shuffle as defined in the problem turns out to be 
# the order of 2 modulo n-1. The sum of n st. this divides 60 is then 
# sigma1(2**60 - 1) + sigma0(2**60 - 1),
# and the sum of n st. this is exactly 60 can then be found by PIE. Factoring
# numbers of the form 2**k - 1 is relatively easy, which makes computing the
# sigma-functions relatively easy.

prime_bound = 10**4
factorization.generate_default_primes_and_hints(prime_bound)

def merge(pp1, pp2):
    # Note: This modifies the inputs, and should therefore not be exported
    # in its current form
    result = []
    while pp1 and pp2:
        p1, k1 = pp1[-1]
        p2, k2 = pp2[-1]
        if p1 > p2:
            result.append(pp1.pop())
        elif p2 > p1:
            result.append(pp2.pop())
        else:
            pp1.pop()
            pp2.pop()
            result.append((p1, k1 + k2))
    result.reverse()
    return result + pp1 + pp2

def prime_power_factors_mersenne(n):
    pf_n = prime_factors(n)
    result = []
    for p in pf_n:
        result = merge(result, prime_power_factors((2**n - 1) // (2**(n//p) - 1)))
        n //= p
    return result

def F(n):
    pfp = prime_power_factors_mersenne(n)
    return (prod(sigma_nat_pp(pk, 1) for pk in pfp) 
            + prod(sigma_nat_pp(pk, 0) for pk in pfp))

print(F(60) - F(60//2) - F(60//3) - F(60//5)
      + F(60//6) + F(60//10) + F(60//15)
      - F(60//30))
correct_answer = "3010983666182123972"
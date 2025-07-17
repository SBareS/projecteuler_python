"""
XOR-Primes

We use $x \\oplus y$ for the bitwise XOR of $x$ and $y$.

Define the XOR-product of $x$ and $y$, denoted by $x \\otimes y$, similar to a
long multiplication in base $2$, except that the intermediate results are 
XORed instead of the usual integer addition.

For example, $7 \\otimes 3 = 9$, or in base 2, $111_2 \\otimes 11_2 = 1001_2$:

$$          111_2 $$
$$ \\otimes  11_2 $$
____________________
$$          111_2 $$
$$ \\oplus 111_2  $$
____________________
$$         1001_2 $$

An XOR-prime is an integer $n$ greater than $1$ that is not an XOR-product of
two integers greater than $1$. The above example shows that $9$ is not an 
XOR-prime. Similarly, $5 = 3 \\otimes 4$ is not an XOR-prime. The first few 
XOR-primes are $2, 3, 7, 11, 13, ...$ and the 10th XOR-prime is $41$.

Find the $5 000 000$th XOR-prime.
"""

# This is a roundabout way of asking os for the 5000000'th prime in F2[X]
# (ordered lexicographically, evaluated at 2). These can be generated using
# the sieve of Eratostenes. We can use Gray codes to iterates over the 
# multiples of a given prime without having to do a full multiplication at
# each step.

from itertools import islice


n = 5_000_000
deg_bound = 26 # Bound based on PNT for polynomials over finite fields
sieve_size = 2**(deg_bound + 1)

#Slight optimization: Polynomials with no constant term (except X) are not 
#prime, roughly analogous to how even numbers (except 2) are not prime in Z.
is_prime = [False, True] * (sieve_size // 2)
is_prime[1] = False
is_prime[0b10] = True

for p in range(0b11, 2**(deg_bound//2 + 1), 2): 
    if not(is_prime[p]):
        continue
    degp = p.bit_length() - 1
    for degx in range(degp, deg_bound - degp + 1):
        px = p<<degx
        for t in range(2**degx):
            is_prime[px] = False
            px ^= p * (((t^(t+1)) + 1) >> 1)

primes = (p for p, b in enumerate(is_prime) if b)
print(next(islice(primes, n-1, None)))

correct_answer = "124136381"
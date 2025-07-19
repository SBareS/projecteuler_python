"""
XOR-Powers

We use $x \\oplus y$ for the bitwise XOR of $x$ and $y$.

Define the XOR-product of $x$ and $y$, denoted by $x \\otimes y$, similar to a
long multiplication in base $2$, except that the intermediate results are 
XORed instead of the usual integer addition.

For example, $11 \\otimes 11 = 69$, or in base 2, 
$1011_2 \\otimes 1011_2 = 1000101_2$:

$$            1011_2 $$
$$ \\otimes   1011_2 $$
_______________________
$$            1011_2 $$
$$ \\oplus   1011_2  $$
$$ \\oplus 1011_2    $$
_______________________
$$         1000101_2 $$

Further we define $P(n) = 11^{\\otimes n} = 11 \\otimes \\dots \\otimes 11$. 
For example $P(2) = 69$.

Find $P(8^{18} 12^8)$. Give your answer modulo $10^9 + 7$.
"""

# We're essentially asked to raise a polynomial over F2 to a large power and
# evaluate it at 2 modulo 10**9 + 7. All powers of 2 from the polynomial can
# "pulled in" using the Freshman's Dream f(x)^(2^a * b) == f(x^(2^a)) * b.

from polynomials import polymul_f2

the_mod = 10**9 + 7

nu2 = 12*3 + 8*2
nu3 = 8

poly = 11
for _ in range(nu3):
    poly = polymul_f2(polymul_f2(poly, poly), poly)

x = pow(2, 2**nu2, the_mod)
result = sum(pow(x, i, the_mod) for i in range(poly.bit_length()) if poly & (1<<i)) % the_mod
print(result)

correct_answer = "14063639"
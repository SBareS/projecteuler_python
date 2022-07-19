"""
Prime permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of 
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
primes, exhibiting this property, but there is one other 4-digit 
increasing sequence.

What 12-digit number do you form by concatenating the three terms in 
this sequence?
"""

from primes import eratos_lt


is_prime = eratos_lt(10**4)

def find_answer():
    for a in range(10**3, 10**4):
        if is_prime[a]:
            for step in range(1, (10**4 - 1 - a)//2):
                if (a, step) == (1487, 3330):
                    # Case from problem description; 
                    # not the one we ar interested in
                    continue
                
                b = a + step
                c = b + step
                if (is_prime[b] and is_prime[c] and 
                    sorted(str(a)) == sorted(str(b)) == sorted(str(c))):
                    return int (str(a) + str(b) + str(c))

print(find_answer())
correct_answer = "296962999629"
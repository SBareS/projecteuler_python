"""
Totient maximum
Euler's Totient function, φ(n) [sometimes called the phi function], is
used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine'
and relatively prime to nine, φ(9)=6.

n 	Relatively Prime 	φ(n) 	n/φ(n)
2 	1 	                1 	    2
3 	1,2 	            2 	    1.5
4 	1,3 	            2 	    2
5 	1,2,3,4 	        4 	    1.25
6 	1,5 	            2 	    3
7 	1,2,3,4,5,6 	    6 	    1.1666...
8 	1,3,5,7 	        4 	    2
9 	1,2,4,5,7,8 	    6 	    1.5
10 	1,3,7,9 	        4 	    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

# p**k / phi(p**k) = p**k / ((p-1)*p**(k-1)) = p / (p-1), so n / phi(n)
# is the product of p / (p-1) over the unique prime factors of n. The 
# goal is then to have each of these factors as big as possible (i.e. 
# small primes), and to have as many factors as possible. It is easily 
# seen that this is achieved simply by taking the product of the first
# few primes.

from primes import primes_seq


result = 1
for p in primes_seq():
    if result * p > 10**6:
        break
    result *= p

print(result)
correct_answer = "510510"
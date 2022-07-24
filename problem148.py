"""
Exploring Pascal's triangle
We can easily verify that none of the entries in the first seven rows of
Pascal's triangle are divisible by 7:
  	  	  	  	  	  	 1
  	  	  	  	  	 1 	  	 1
  	  	  	  	 1 	  	 2 	  	 1
  	  	  	 1 	  	 3 	  	 3 	  	 1
  	  	 1 	  	 4 	  	 6 	  	 4 	  	 1
  	 1 	  	 5 	  	10 	  	10 	  	 5 	  	 1
1 	  	 6 	  	15 	  	20 	  	15 	  	 6 	  	 1

However, if we check the first one hundred rows, we will find that only
2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one
billion (109) rows of Pascal's triangle.
"""

from math import prod
from digits import digits


# From Kummer's theorem, it follows that the the n-k'th bonimial 
# coefficient is divisible by p iff any of the base-p digits of k are
# larger than the corresponding base-p digit of n. Now do some tricks
# to make the summation sublinear
N = 10**9
N_digs = digits(N, 7)

pow7_results = [1]

for i in range(len(N_digs) - 1):
    pow7_results.append(pow7_results[-1] * 7*8 // 2)

result = 0
# Now we increase the digits from left to right until we get to N
for i, d in enumerate(N_digs):
    left = N_digs[:i]
    right = N_digs[i+1:]

    # Rows with i'th digit less than d
    result += d * (d+1) // 2 * prod(x+1 for x in left) * pow7_results[-i - 1]

print(result)
correct_answer = "2129970655314432"
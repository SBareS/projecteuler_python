"""
Pandigital products
We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 
pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

from itertools import permutations

from digits import digits, undigits

pandigital_products = set()
digs = list(range(1, 10))
digs_set = set(digs)

# if a * b = c, then 
#    #(digits in c) - 1 = #(digits in a) - 1 + (#digits in b) - 1
# or #(digits in c) - 1 = #(digits in a) - 1 + (#digits in b) - 1 + 1
# it's then easy to see that the number of digits in a, b, c 
# respectively must be either 1, 4, 4 or 2, 3, 4

for p in permutations(digs, 5):
    remaining_digits = digs_set - set(p)

    # 1, 4, 4 digits
    a = p[0]
    b = undigits(p[1:5])
    c = a * b
    c_digs = digits(c)
    if len(c_digs) == 4 and set(c_digs) == remaining_digits:
        pandigital_products.add(c)
    
    # 2, 3, 4 digits
    a = undigits(p[0:2])
    b = undigits(p[2:5])
    c = a * b
    c_digs = digits(c)
    if len(c_digs) == 4 and set(c_digs) == remaining_digits:
        pandigital_products.add(c)

print(sum(pandigital_products))
correct_answer = "45228"
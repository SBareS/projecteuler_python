"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit 
numbers.
"""

def is_palindromic(n):
    str_n = str(n)
    return str_n == str_n[::-1]

largest_palindrome_product = max(i*j 
    for i in range(100, 1000) 
    for j in range(i, 1000) 
    if is_palindromic(i*j))

print(largest_palindrome_product)
correct_answer = "906609"
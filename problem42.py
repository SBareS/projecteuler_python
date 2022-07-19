"""
Coded triangle numbers
The nth term of the sequence of triangle numbers is given by, 
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text 
file containing nearly two-thousand common English words, how many are 
triangle words?
"""

from math import isqrt


with open("data/p042_words.txt") as file:
    words = list(map(lambda s: s[1:len(s)-1], file.read().split(',')))
words.sort()

def char_value(c):
    return ord(c) - ord('A') + 1

def word_value(word):
    return sum(char_value(c) for c in word)

def is_square(n):
    return isqrt(n)**2 == n

def is_triangle(n):
    # n = k*(k-1)/2 is equivalent to k = (-1 +- sqrt(8*k + 1))/2, which
    # is an integer if and only if 8*K + 1 is a square.
    return is_square(8*n + 1)

print(sum(is_triangle(word_value(w)) for w in words))
correct_answer = "162"
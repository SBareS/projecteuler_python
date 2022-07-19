""""
If the numbers 1 to 5 are written out in words: one, two, three, four, 
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in 
compliance with British usage.
"""

ones_words = ["", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens_words = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", 
    "seventy", "eighty", "ninety"]

def number_word_length(n):
    if 1 <= n < 20:
        return len(ones_words[n])
    elif 20 <= n < 100:
        tens, ones = divmod(n, 10)
        return len(tens_words[tens]) + len(ones_words[ones])
    elif 100 <= n < 1000:
        hundreds, rest = divmod(n, 100)
        result = len(ones_words[hundreds]) + len("hundred")
        if rest != 0:
            result += len("and")
            result += number_word_length(rest)
        return result
    elif n == 1000:
        return len("onethousand")
    else:
        raise ValueError("Only numbers in range [1, 1000] are supported")

print(sum(number_word_length(n) for n in range(1, 1001)))
correct_answer = "21124"
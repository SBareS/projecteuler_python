"""
Passcode derivation
A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode
was 531278, they may ask for the 2nd, 3rd, and 5th characters; the
expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse
the file so as to determine the shortest possible secret passcode of
unknown length.
"""

from collections import Counter


with open("data/p079_keylog.txt") as file:
    lines = [s.strip() for s in file.readlines()]

# Heuristic statistical strategy: Look at the first character on each 
# line; the most common one is the one most likely to be the first
# character in the passcode, so let that be our guess for the first
# character. Then remove this character from each of the strings and 
# repeat (removing empty strings from the list at each step), until 
# there is no more data left.
guessed_chars = []
while lines:
    first_letter_counts = Counter(s[0] for s in lines)
    if len(first_letter_counts) > 1:
        most_common = first_letter_counts.most_common(2)
        if most_common[0][1] > most_common[1][1]:
            c = most_common[0][0]
        else:
            # Break ties with fewest last-letter occurrences
            last_letter_counts = Counter(s[-1] for s in lines)
            c = min(most_common[0][0], most_common[1][0], key=last_letter_counts.__getitem__)
    else:
        c = first_letter_counts.most_common(1)[0][0]
    guessed_chars.append(c)

    new_lines = []
    for s in lines:
        s = s.replace(c, '')
        if s:
            new_lines.append(s)
    lines = new_lines

passcode_guess = ''.join(guessed_chars)

print(passcode_guess)
correct_answer = "73162890"
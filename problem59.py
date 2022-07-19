"""
XOR decryption
Each character on a computer is assigned a unique code and the preferred
 standard is ASCII (American Standard Code for Information Interchange).
 For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption
key on the cipher text, restores the plain text; for example, 
65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the 
modified method is to use a password as a key. If the password is 
shorter than the message, which is likely, the key is repeated 
cyclically throughout the message. The balance for this method is using
a sufficiently long password key for security, but short enough to be
memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using p059_cipher.txt (right click and 
'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English
words, decrypt the message and find the sum of the ASCII values in the
original text.
"""

from collections import Counter
from itertools import cycle

from comb_it import cyclic_permutations

def xor_cipher(data, key):
    return[d ^ k for d, k in zip(data, cycle(key))]

def frequency_analysis(encrypted, word, key_length):
    word_ascii = [ord(c) for c in word]
    counters = [Counter() for _ in range(key_length)]
    for w in cyclic_permutations(word_ascii):
        xored = xor_cipher(encrypted, w)
        for i in range(key_length):
            counters[i].update(xored[i::key_length])
    return counters

with open("data/p059_cipher.txt") as file:
    encrypted = list(map(int, file.read().split(',')))

freqs = [Counter(), Counter(), Counter()]
for f_old, f_new in zip(freqs, frequency_analysis(encrypted, " ", 3)):
    f_old.update(f_new)
for f_old, f_new in zip(freqs, frequency_analysis(encrypted, "the", 3)):
    f_old.update(f_new)

key_guess = [f.most_common(1)[0][0] for f in freqs]
#print("Key guess: ", *map(chr, key_guess), sep='')
#print("\nDecrypted text: \n", *map(chr, xor_cipher(encrypted, key_guess)), sep='')

print(sum(xor_cipher(encrypted, key_guess)))
correct_answer = "129448"
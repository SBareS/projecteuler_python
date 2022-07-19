"""
Longest Collatz sequence
The following iterative sequence is defined for the set of positive 
integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following 
sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz 
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one 
million.
"""


N = 10**6
memo = N * [None]

def collatz_next(n):
    return n // 2 if n % 2 == 0 else 3*n + 1

memo[1] = 1
for i in range(2, N):
    seq = []
    x = i
    while x >= N or memo[x] is None:
        seq.append(x)
        x = collatz_next(x)
    seq_len = memo[x]
    for x in reversed(seq):
        seq_len += 1
        if x < N:
            memo[x] = seq_len

print(max(range(1, N), key=memo.__getitem__))
correct_answer = "837799"
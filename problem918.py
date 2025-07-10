"""
Recursive Sequence Summation

The sequence $a_n$ is defined by $a_1 = 1$, and then recursively for 
$n \\ge 1$:
$$a_{2n} = 2a_n$$
$$a_{2n+1} = a_n - 3a_{n+1}$$

The first ten terms are 1, 2, -5, 4, 17, -10, -17, 8, -47, 34.
Define $S(N) = \\sum_{n=1}^N a_n$. You are given $S(10) = -13$.
Find $S(10^{12})$. 
"""

# By manipulating the sum a little and using the recursion, one finds that
# S(N) = 4 - a_N/2 for N even. a_N/2 can be computed quickly directly using
# its recursion, even without memoization. With memoization, it is nearly
# instantaneous.

from functools import cache

@cache
def a(n):
    if n == 1:
        return 1
    return 2 * a(n//2) if n % 2 == 0 else a(n//2) - 3*a(n//2 + 1)

N = 10**12
print(4-a(N//2))

correct_answer = "-6999033352333308"
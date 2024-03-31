"""
Not Zeckendorf
Consider the Fibonacci sequence {1, 2, 3, 5, 8, 13, 21, ...}.

We let f(n) be the number of ways of representing an integer n>=0 as the sum
of different Fibonacci numbers.
For example, 16 = 3 + 13 = 1 + 2 + 13 = 3 + 5 + 8 = 1 + 2 + 5 + 8 and hence 
f(16) = 4. By convention f(0) = 1.

Further we define S(n) = f(0) + ... + f(n).
You are given and S(100) = 415 and S(10^4) = 312807.

Find S(10^13).
"""
N = 10**13

fib = [1, 2]
while fib[-1] < N:
    fib.append(fib[-1] + fib[-2])
fibsums = [0]
for f in fib:
    fibsums.append(fibsums[-1] + f)

def S(N, i):
    if N == 0:
        return 1
    if i < 0 or N < 0:
        return 0
    
    result = 0

    # Sums not involving containing fib[i]
    if fibsums[i] <= N:
        result += 2**i      #In this case all sums involving fib[0], ..., fib[i-1] are possible
    else:
        result += S(N, i-1) #In this case, we need to recurse

    # Sums infolving fib[i] (if possible)
    if fib[i] <= N:
        result += S(N - fib[i], i-1)
    return result

print(S(N, len(fib)-2))
correct_answer = "2877071595975576960"
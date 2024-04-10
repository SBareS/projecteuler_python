r"""
Let $a_k$, $b_k$, and $ck$ represent the three solutions (real or complex 
numbers) to the equation $\frac{1}{x} = (\frac{k}{x})^2 (k + x^2) - kx$.

For instance, for $k = 5$, we see that $\{a_5, b_5, c_5\}$ is approximately
$\{5.727244, -0.363622+2.057397i, -0.363622-2.057397i\}$.

Let $S(n) = \sum_{p=1}^n \sum_{k=1}^n (a_k + b_k)^p(b_k + c_k)^p(c_k + a_k)^p$.

Interestingly, $S(n)$ is always an integer. For example, $S(4) = 51160$.

Find $S(10^6)$ modulo $1 000 000 007$
"""

themod = 1_000_000_007

def sum_p(n, k):
    r = (1 - k**2)%themod
    return (r - pow(r, n+1, themod)) * pow(k, -2, themod)

def S(n):
    return sum(sum_p(n, k) for k in range(1, n+1)) % themod

print(S(10**6))
correct_answer = "191541795"
"""
Prime Factor and Exponent

For a positive integer n > 1, let p(n) be the smallest prime dividing n, and
let $\\alpha(n)$ be its p-adic order, i.e. the largest integer such that 
$p(n)^{\\alpha(n)}$ divides n.

For a positive integer K, define the function f_K(n) by:
$$f_K(n) = \\frac{\\alpha(n) - 1}{(p(n))^K}$$
Also define f_K by:
$$f_K = \\lim_{N \\to \\infty}\\sum_{n=2}^N f_K(n)$$
It can be verified that $f_1 \\approx 0.282419756159$.

Find $\\sum_{K=1}^\\infty f_K$. Give your answer rounded to 12 digits after 
the decimal point.
"""

# What we are computing is an asymptotic mean, so we can treat p(n) as a 
# random variable taking the value p_i with probability
# t_i := (1 - 1/2) * (1 - 1/3) * ... * (1 - 1/p_{i-1}) * 1/p_i.
# Conditioned on p(n) = p_i, the (asymptotic) mean of alpha(n)-1
# 1/p_i + 1/p_i^2 + ... = 1/(p_i - 1),
# So the total contribution of p_i to the sum is
#   t_i * 1/(p_i - 1) * (1/p_i + 1/p_i^2 + ... = 1/(p_i - 1))
# = t_i * 1/(p_1 - 1) * 1/(p_1 - 1)
# Luckily t_i approaches 0 reasonably quickly, so the whole sum converges
# reasonably quickly.

from primes import primes_lt


primes = primes_lt(10**5)

result = 0
prob = 1
for p in primes:
    result += prob/p/(p-1)/(p-1)
    prob *= 1 - 1/p
print(f"{result:.12f}")

correct_answer = "0.547326103833"
"""
Counting Binary Quadratic Representations

Let g(n) denote the number of ways a positive integer n can be represented in
the form x^2 + xy + 41y^2 where x and y are integers. For example, g(53) = 4
due to $(x, y) \\in \\{(-4, 1), (-3, -1), (3, 1), (4, -1)\\}.

Define $T(N) = \\sum_{n=1}^N g(n)$. You are given T(10^3) = 747 and 
T(10^6) = 492128.

Find T(10^16).
"""

# The quadratic form in question is the norm of the quadratic number field with
# discriminant -163; so we simply need to count lattice points within a disk. 
# The fact that the class number is 1 is a red herring: The same technique 
# works for any positive definite quadratic form.

from math import ceil, floor, isqrt, sqrt

N = 10**16
omega_im = sqrt(163)/2

result = 2 * isqrt(N) # Points on real line
for y in range(1, floor(sqrt(N) / omega_im) + 1):
    re = -y / 2
    im = y * omega_im
    max_re = sqrt(N - im**2)
    max_x = floor(max_re - re)
    min_x = ceil(-max_re - re)
    result += max(max_x - min_x + 1, 0) * 2

print(result)

correct_answer = "4921370551019052"
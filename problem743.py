"""
Window into a Matrix
A window into a matrix is a contiguous sub matrix.

Consider a 2xn matrix where every entry is either 0 or 1.
Let A(k, n) be the total number of these matrices such that the sum of
the entries in every window is k.

You are given that A(3, 9) = 560 and A(4, 20) = 1060870.

Find $A(10^8, 10^{16})$. Give your answer modulo 1 000 000 007
"""

from mod_arith import inverse_table

# Note: This solution runs in about 90 seconds on my shitty laptop using
# CPython. It would probably be confortably below 90 seconds on better 
# hardware (e.g. my desktop) and/or with a jitted interpreter (e.g. PyPy)

themod = 1_000_000_007

inverses = inverse_table(themod, 10**8//2 + 1)

def A(k, n):
    # Assumes k divides n
    # Number of columns with two zeros must be the same as the number of
    # columns with two ones. The remaining columns will have one zero 
    # and one one, giving 2 choices for each.
    # When sliding the window over, we have only one choice when a 
    # double-zero or a double-one leaves the window, but two choices 
    # when a zero-one or one-zero leaves the window. This gives a 
    # formula:
    # A(k, n) = sum(i = 0 to k//2) trinom(k, i, i, (k-2i)) * 2**(n - 2*i*(n//k))
    result = 0
    next_term = pow(2, n, themod)
    pow2_inv_factor = pow(inverses[2], (2*(n // k)), themod)
    for i in range(k // 2 + 1):
        #result = (result + k_choose_twoi * twoi_choose_i * big_pow2) % themod
        result = (result + next_term) % themod
        next_term = next_term * (k - 2*i) * (k - 2*i - 1) * inverses[i + 1]**2 * pow2_inv_factor % themod
    return result

print(A(10**8, 10**16))
correct_answer = "259158998"
"""
Pizza Toppings
You are given a pizza (perfect circle) that has been cut into m*n equal pieces
and you want to have exactly one topping on each slice.

Let f(m, n) denote the number of ways you can have toppings on the pizza with m
different toppings (m >= 2), using each topping on exactly n slices (n >= 1).
Reflections are considered distinct, rotations are not.

Thus, for instance, f(2, 1) = 1, f(2, 2) = f(3, 1) = 2 and f(3, 2) = 16.

is shown below:
[illustration]

Find the sum of all f(m, n) such that f(m, n) <= 10^15.
"""

from arithfunct import euler_phi_pp, multfunc_table

N = 10**15

# These bounds can be checked using some rough pen-and-paper estimates
m_bound = 19
n_bound = 30
mn_bound = (n_bound-1)*(m_bound-1)

phi_tab = multfunc_table(euler_phi_pp, n_bound+1)
fact_tab = [1]
for i in range(1, mn_bound + 1):
    fact_tab.append(i * fact_tab[-1])

def f(m, n):
    # Simple use of Burnside's Lemma
    return sum(phi_tab[n // d] * fact_tab[m*d]//fact_tab[d]**m for d in range(1, n+1) if n % d == 0)//(m*n)

print(sum(ff for m in range(2, m_bound) for n in range(1, n_bound) if (ff := f(m, n)) <= N))
correct_answer = "1485776387445623"
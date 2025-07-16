import factorization

from comb_it import sublists_be
from factorization import prime_power_factors
from mod_arith import orth_idemp

N = 10**7
factorization.generate_default_hints(N+1)
def M(n):
    pp = [p**k for (p, k) in prime_power_factors(n)]
    return max(sum(L) % n for L in sublists_be(orth_idemp(pp)))

print(sum(M(n) for n in range(1, N+1)))
correct_answer = "39782849136421"
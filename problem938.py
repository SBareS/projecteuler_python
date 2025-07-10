"""
Exhausting a Colour

A deck of cards contains r red cards and b black cards.
A card is chosen uniformly randomly from the deck and removed. A second card 
is then chosen uniformly randomly from the cards remaining and removed.

* If both cards are red, they are discarded.
* If both cards are black, they are both put back in the deck.
* If they are different colours, the red card is put back in the deck and the 
    black card is discarded.

Play ends when all the remaining cards in the deck are the same colour and let P(r, b) 
be the probability that this colour is black.

You are given P(2, 2) = 0.4666666667, P(10, 9) = 0.4118903397 and 
P(34, 25) = 0.3665688069.

Find P(24690, 12345). Give your answer with 10 digits after the decimal point.
"""

# Note r = 2b in our case. Letting P(n) = P(2n, n), one has
# P(n) = (4 * (2*n - 1)**2 * P(n-1) - 1)/(16*n**2 - 16*n + 3)
# (credit to griff on the forum for noticing this. The formula is of course 
# easy to derive once one has the idea.)

# result = 1/3 # = P(2, 1)
# for n in range(2, 12345 + 1):
#     result = (4 * (2*n - 1)**2 * result - 1)/(16 * n**2 - 16 * n + 3)

# The recursion even admits an exact solution in terms of the gamma function:
# P(n) = 1 - (2**(2*n-1) * Gamma(n + 1/2))/(sqrt(pi) * Gamma(1/2 + 2*n)).
# The huge intermediate values can be avoided by taging logs.

from math import exp, lgamma, log, pi

n = 12345

result = 1 - exp((2*n-1)*log(2) + 2*lgamma(n + 0.5) - 0.5*log(pi) - lgamma(0.5 + 2*n))
print(f"{result:.10f}")

correct_answer = "0.2928967987"
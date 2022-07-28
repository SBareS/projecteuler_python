"""
Monopoly odds
In the game, Monopoly, the standard board is set up in the following 
way:
[...]
A player starts on the GO square and adds the scores on two 6-sided
dice to determine the number of squares they advance in a clockwise
direction. Without any further rules we would expect to visit each
square with equal probability: 2.5%. However, landing on G2J (Go To
Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders
the player to go directly to jail, if a player rolls three
consecutive doubles, they do not advance the result of their 3rd roll.
Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a
player lands on CC or CH they take a card from the top of the respective
pile and, after following the instructions, it is returned to the bottom
of the pile. There are sixteen cards in each pile, but for the purpose
of this problem we are only concerned with cards that order a movement;
any instruction not concerned with movement will be ignored and the
player will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a
particular square. That is, the probability of finishing at that square
after a roll. For this reason it should be clear that, with the
exception of G2J for which the probability of finishing on it is zero,
the CH squares will have the lowest probabilities, as 5/8 request a
movement to another square, and it is the final square that the player
finishes at on each roll that we are interested in. We shall make no
distinction between "Just Visiting" and being sent to JAIL, and we shall
also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39
we can concatenate these two-digit numbers to produce strings that
correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in
order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
(3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find
the six-digit modal string.
"""

from collections import defaultdict

from itertools import product

from dgraph import WeightedHalfEdge, markov_chain_stationary_distribution

# The problem can be solved by Markov-chain methods. Strictly speaking, 
# we make one incorrect assumption, namely that the draws from Community
# Chest and Chance are independent (this is not the case, since the 
# drawn card is returned to the bottom). However, this won't affect the
# overall densities that much - the reason being that the ergodic mixing
# should happen much faster than one is likely to land on CC/CH several
# times in a row. As such, the rankings (at least of the most likely few
# squares) will still be correct.

board = [
    'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 
    'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
    'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
    'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
board_size = len(board)  # = 40

transitions = defaultdict(lambda: 0)
dice_sides = 4

def next_startingwith(i, prefix):
    for square in board[i:]:
        if square.startswith(prefix):
            return square
    for square in board:
        if square.startswith(prefix):
            return square
    assert False, "Should never reach this place"

for start_ind, start in enumerate(board):
    for doubles_start in range(3):
        for d1, d2 in product(range(1, dice_sides+1), repeat=2):
            p = dice_sides**(-2)
            start_state = start, doubles_start
            if d1 == d2:
                doubles_end = doubles_start + 1
            else:
                doubles_end = 0
            
            if doubles_end == 3:
                end = 'JAIL'
                doubles_end = 0
            else:
                end_ind = (start_ind + d1 + d2) % board_size
                end = board[end_ind]
            
            if end == 'G2J':
                end = 'JAIL'
                doubles_end = 0
            
            elif end.startswith('CC'):
                transitions[start_state, ('GO', doubles_end)] += p * 1/16
                transitions[start_state, ('JAIL', 0)] += p * 1/16
                p *= 14/16
            
            elif end.startswith('CH'):
                transitions[start_state, ('GO', doubles_end)] += p * 1/16
                transitions[start_state, ('JAIL', 0)] += p * 1/16
                transitions[start_state, ('C1', doubles_end)] += p * 1/16
                transitions[start_state, ('E3', doubles_end)] += p * 1/16
                transitions[start_state, ('H2', doubles_end)] += p * 1/16
                transitions[start_state, ('R1', doubles_end)] += p * 1/16
                transitions[start_state, (next_startingwith(start_ind, 'R'), doubles_end)] += p * 2/16
                transitions[start_state, (next_startingwith(start_ind, 'U'), doubles_end)] += p * 1/16

                three_back = board[(end_ind - 3) % board_size]
                if three_back.startswith('CC'):  # three back from CH3 lands on CC3
                    transitions[start_state, ('GO', doubles_end)] += p * 1/16 * 1/16
                    transitions[start_state, ('JAIL', 0)] += p * 1/16 * 1/16
                    transitions[start_state, (three_back, doubles_end)] += p * 1/16 * 14/16
                else:
                    transitions[start_state, (three_back, doubles_end)] += p * 1/16
                
                p *= 6/16

            transitions[start_state, (end, doubles_end)] += p

MK = defaultdict(list)
for (start_state, end_state), p in transitions.items():
    MK[start_state].append(WeightedHalfEdge(end_state, p))

stationary_distribution = markov_chain_stationary_distribution(MK)
square_probs = defaultdict(lambda: 0)
for (square, _), p in stationary_distribution.items():
    square_probs[square] += p

ordered_squares = [k for k, v in sorted(square_probs.items(), key=lambda x: -x[1])]
square_numbers = {s: f"{i:02}" for (i, s) in enumerate(board)}

result = ''.join(square_numbers[s] for s in ordered_squares[:3])
print(result)
correct_answer = "101524"
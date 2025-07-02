"""
Poker hands
In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards
are compared, and so on.

Consider the following five hands dealt to two players:

[...]

The file, poker.txt, contains one-thousand random hands dealt to two 
players. Each line of the file contains ten cards (separated by a single
space): the first five are Player 1's cards and the last five are 
Player 2's cards. You can assume that all hands are valid (no invalid 
characters or repeated cards), each player's hand is in no specific 
order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from collections import Counter


class Card:
    __slots__ = "value", "suit"
    def __init__(self, s : str):
        number, suit = s
        self.value = "123456789TJQKA".index(number)
        self.suit = suit
    def short_str(self) -> str:
        return "123456789TJQKA"[self.value] + self.suit
    def __repr__(self) -> str:
        return f"Card({self.short_str()})"

class Hand:
    HIGH_CARD       = 0
    ONE_PAIR        = 1
    TWO_PAIRS       = 2
    THREE_OF_A_KIND = 3
    STRAIGHT        = 4
    FLUSH           = 5
    FULL_HOUSE      = 6
    FOUR_OF_A_KIND  = 7
    STRAIGHT_FLUSH  = 8
    # ROYAL_FLUSH     = 9  # Special case of straight flush

    __slots__ = "cards",

    def __init__(self, s : str):
        self.cards = list(map(Card, s.split()))
        if len(self.cards) != 5:
            raise ValueError("Could not parse card")
    def hand_value(self):
        # Check for flush
        c0 = self.cards[0]
        is_flush = all(c.suit == c0.suit for c in self.cards)
        
        # Check for straight
        sorted_vals = sorted(c.value for c in self.cards)
        last_value = sorted_vals[0]
        for v in sorted_vals[1:]:
            if v != (last_value + 1) % 13:
                is_straight = False
                break
            last_value = v
        else:
            is_straight = True
        
        # Sort cards descending, so as to be useful for comparison
        sorted_vals = tuple(sorted_vals[::-1])
        
        if is_straight and is_flush:
            return (Hand.STRAIGHT_FLUSH, -1, -1, sorted_vals)
        
        counts = Counter(sorted_vals).most_common()
        if counts[0][1] == 4:
            return (Hand.FOUR_OF_A_KIND, counts[0][0], -1, sorted_vals)
        
        if counts[0][1] == 3 and counts[1][1] == 2:
            return (Hand.FULL_HOUSE, counts[0][0], counts[1][0], sorted_vals)
        
        if is_flush:
            return (Hand.FLUSH, -1, -1, sorted_vals)
        
        if is_straight:
            return (Hand.STRAIGHT, -1, -1, sorted_vals)
        
        if counts[0][1] == 3:
            return (Hand.THREE_OF_A_KIND, counts[0][0], -1, sorted_vals)
        
        if counts[0][1] == counts[1][1] == 2:
            return (Hand.TWO_PAIRS, counts[0][0], counts[1][0], sorted_vals)
        
        if counts[0][1] == 2:
            return (Hand.ONE_PAIR, counts[0][0], -1, sorted_vals)
        
        return (Hand.HIGH_CARD, -1, -1, sorted_vals)

    def __lt__(self, other):
        return self.hand_value() < other.hand_value()
    
    def __repr__(self) -> str:
        return f"Hand({' '.join(c.short_str() for c in self.cards)})"

result = 0
with open("data/p054_poker.txt") as file:
    for line in file.readlines():
        hand1 = Hand(line[:14])
        hand2 = Hand(line[15:])
        if hand1 > hand2:
            result += 1

print(result)
correct_answer = "376"
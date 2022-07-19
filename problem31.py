"""
Coin sums
In the United Kingdom the currency is made up of pound (£) and pence 
(p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can £2 be made using any number of coins?
"""

from functools import cache


def change_possibilities(n, coins):
    @cache
    def rec(n, coin_ind):
        if n == 0:
            return 1
        if n < 0 or coin_ind >= len(coins):
            return 0
        
        rec_result = [rec(n - coins[coin_ind], coin_ind)]
        for i, coin in enumerate(coins[coin_ind+1:], coin_ind+1):
            rec_result.append(rec(n - coin, i))
        
        return sum(rec_result)
    return rec(n, 0)

print(change_possibilities(200, [1, 2, 5, 10, 20, 50, 100, 200]))
correct_answer = "73682"
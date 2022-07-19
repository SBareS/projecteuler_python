"""
Reciprocal cycles
A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It 
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""

from functools import partial

# Solution adapted from my earlier F#-solution, hence the 
# functional-ish style

def cycle_length(f, x0):
    tortoise = x0
    hare = f(x0)

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    
    result = 1
    while (hare := f(hare)) != tortoise:
        result += 1
    
    return result

def step(den, rd):
    rem, _ = rd
    q, r= divmod(rem, den)
    return r * 10, q

def reciprocal_cycle_length(den):
    return cycle_length((partial(step, den)), (1, 0))

print(max(range(1, 1000), key=reciprocal_cycle_length))
correct_answer = "983"
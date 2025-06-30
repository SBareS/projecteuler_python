"""
Problem Heegner

Among all non-square integers with absolute value not exceeding 10^3, find the
value of such that is closest to an integer.
"""

# The hint is in the name: exp(pi*sqrt(163)) happens to be super-duper close
# to an (even) integer; this is because 163 is a Heegner number and 
# exp(pi*sqrt(163)) + 744 is extremely close to the singular modulus 
# j((1+sqrt(163))/2). Therefore, cos(pi*sqrt(-163)), being super-duper close
# to exp(pi*sqrt(163))/2 is also super-duper close to an integer.

print(-163)
correct_answer = "-163"
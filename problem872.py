"""
Recursive Tree

A sequence of rooted trees Tn is constructed such that Tn has nodes numbered 1
to n.

The sequence starts at T1, a tree with a single node as a root with the 
number 1.

For n > 1, Tn is constructed from T(n-1) using the following procedure:

1. Trace a path from the root of T(n-1) to a leaf by following the 
largest-numbered child at each node.
2. Remove all edges along the traced path, disconnecting all nodes along it 
from their parents.
3. Connect all orphaned nodes directly to a new node numbered n, which becomes
the root of Tn.

For example, the following figure shows T6 and T7. The path traced through 
during the construction of is coloured red.

(image)

Let f(n, k) be the sum of the node numbers along the path connecting the root
of Tn to the node k, including the root and the node k. For example, 
f(6, 1) = 6 + 5 + 1 and f(10, 3) = 29.

Find f(10^17, 9^17).
"""

# The parent of k in Tn is the largest number of the form k + 2**r 
# with k + 2**r <= n.

n = 10**17
k = 9**17

result = k
while k < n:
    pow2 = 1
    while k + 2*pow2 <= n:
        pow2 *= 2
    k += pow2
    result += k
print(result)

correct_answer = "2903144925319290239"
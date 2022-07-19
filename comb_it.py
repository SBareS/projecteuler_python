"""Contains some combinatoric iterables."""

from itertools import chain, product, starmap


def cyclic_permutations(L):
    """Iterates over all cyclic permutations of the list (or string, or
    other slicable with length) L"""
    for i in range(len(L)):
        yield L[i:] + L[:i]

def integer_partitions(n, m=1):
    """Iterates over all partitions of the integer n into sums of 
    integers each at least equal to m (default 1). Each partition is
    given as an increasing list of integers."""
    yield [n]
    for i in range(m, n//2 + 1):
        for p in integer_partitions(n-i, i):
            yield [i] + p

def sublists_be(L):
    """Iterates over all sublists of the list L. In principle, the input
    can be any finite iterable, but the results will always be lists. 
    The subsets are yielded in big-endian binary-counting order, i.e. 
    sublists([1,2,3]) yields [] [3] [2] [2,3] [1] [1,3] [1,2] [1,2,3]"""
    for list_of_lists in product(*(([], [x]) for x in L)):
        yield list(chain(*list_of_lists))
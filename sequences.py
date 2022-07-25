"""Contains some sequences and tools for dealing with sequences."""

from heapq import heapify, heappop, heappush, heapreplace
from itertools import count, islice
from math import inf

def nth(s, n):
    """Returns the nth element (zero-indexed) of the sequence s. If s
    has less than n+1 elements, throws an IndexError"""
    try:
        return next(islice(s, n, None))
    except StopIteration:
        raise IndexError("Sequence shorter than the given index.")

def intersection(*seqs):
    """Yields the intersection of the given (weakly) increasing 
    sequences (given as iterables). Note: non-increasing sequences will
     not work!"""
    its = tuple(map(iter, seqs))

    # Special cases
    if len(its) == 0:
        raise ValueError("Should have at least one sequence (don't know \
                          what to do by default with zero sequences)")
    if len(its) == 1:
        return its[0]
    
    heap = [(next(s), i) for i, s in enumerate(its)]
    heapify(heap)
    
    while True:
        n0 = heap[0][0]
        if all(n == n0 for n, _ in heap):
            yield n0
            try:
                heap = [(next(s), i) for i, s in enumerate(its)]
            except StopIteration:
                return  # One of the sequences ran out.
            heapify(heap)
        else:
            while heap[0][0] == n0:
                _, i = heap[0]
                heapreplace(heap, (next(its[i]), i))

# # Not necessary, this function is implemented in heapq.merge
# # Also, does not handle empty sequences correctly
# def union(*seqs):
#    """Yields the union of the given (weakly) increasing 
#    sequences (given as iterables). Note: non-increasing sequences will
#    not work!"""
#    its = tuple(map(iter, seqs))
#    
#    heap = [(next(s), i) for i, s in enumerate(its)]
#    heapify(heap)
#    
#    while heap:
#        n, i = heappop(heap)
#        yield n
#        try:
#            heappush(heap, (next(its[i]), i))
#        except StopIteration:
#            # One of the sequences ran out, but the others might still 
#            # have more elements
#            pass

def smooth_numbers(primes, upper_bound=None):
    """Yields all numbers (in increasing order) that are only divisble
    by the primes in the given list. Optionally only yields numbers 
    strictly less than upper_bound, which improves memory usage."""
    heap = [(1, inf)]  # x, largest_prime_factor
    while heap:
        x, q = heappop(heap)
        yield x
        for p in primes:
            y = p*x
            if p > q or (upper_bound and y >= upper_bound):
                break
            heappush(heap, (y, p))

def squarefree_numbers(primes, upper_bound=None):
    """Yelds all square-free numbers (in increasing order) that are
    only divisible with the primes in the given list. Optionally only
    yields numbers strictly less than upper_bound, which imrpoves memory
    usage."""
    # Implementation is the same as smooth_numbers up to changing a 
    # single > to >=
    heap = [(1, inf)]  #x, largest_prime_factor
    while heap:
        x, q = heappop(heap)
        yield x
        for p in primes:
            y = p*x
            if p >= q or (upper_bound and y >= upper_bound):
                break
            heappush(heap, (y, p))

class CachedSequence:
    # TODO: 
    #   -Docstring
    #   -Make sure it actually works
    def __init__(self, seq) -> None:
        self._seq = iter(seq)
        self._cache = []

    def __getitem__(self, i : int):
        if i >= len(self._cache):
            try:
                self._extend_cache(i - len(self._cache) + 1)
            except StopIteration:
                raise IndexError("Sequence too short")
        return self._cache[i]
    
    def __iter__(self):
        for i in count():
            if i < len(self._cache):
                yield self._cache[i]
            else:
                try:
                    r = next(self._seq)
                    self._cache.append(r)
                    yield r
                except StopIteration:
                    return
    
    def _extend_cache(self, n) -> None:
        self._cache.extend(next(self._seq) for _ in range(n))
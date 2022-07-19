"""Contains some dynamic programming tools."""

from functools import wraps


_Unpopulated = object()

def cache_nat(initial_size=0, max_size=None):
    """Decorator somewhat simmilar to functools.cache, but for 
    functions taking one natural-number argument. The cache is then 
    stored in a list rather than a dict, which might improve 
    performance in some situations. However, functools.cache will 
    probably still be the fastest in most situations, simply because 
    it is implemented in C."""
    memo = initial_size * [_Unpopulated]
    def decorator(f):
        if max_size == None:
            @wraps(f)
            def wrapper(n):
                if n >= len(memo):
                    memo.extend((n - len(memo) + 1) * [_Unpopulated])

                if memo[n] is _Unpopulated:
                    memo[n] = f(n)
                return memo[n]
            return wrapper
        else:
            @wraps(f)
            def wrapper(n):
                if n >= max_size:
                    return f(n)
                
                if n >= len(memo):
                    memo.extend((n - len(memo) + 1) * [_Unpopulated])

                if memo[n] is _Unpopulated:
                    memo[n] = f(n)
                return memo[n]
            return wrapper
    
    return decorator
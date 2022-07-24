"""Contains some convenience functions and decorators for debugging"""

from functools import wraps
from time import perf_counter


def measure_time(f):
    """Decorator. Prints the time taken to run f."""
    wraps(f)
    def wrapper(*args, **kwargs):
        t0 = perf_counter()
        r = f(*args, **kwargs)
        t1 = perf_counter()
        print(f"Running {f.__name__} took {t1-t0:6g} seconds.")
        return r
    return wrapper

def on_entry_and_exit(on_entry=None, on_exit=None):
    """Decorator. Before calling f, calls on_entry with the arguments 
    given to f. Before returning, calls on_exit with the return value 
    of f. If either function is None, they will be skipped."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if on_entry:
                on_entry(*args, **kwargs)
            r = f(*args, **kwargs)
            if on_exit:
                on_exit(*args, **kwargs)
            return r
        return wrapper
    return decorator

def output_callcount(step=1):
    """Decorator. Outputs the callcount every step calls (so as to 
    indicate progress)."""
    def decorator(f):
        n_calls = 0
        def wrapper(*args, **kwargs):
            nonlocal n_calls
            n_calls += 1
            if n_calls % step == 0:
                print(n_calls)
            return f(*args, **kwargs)
        return wrapper
    return decorator
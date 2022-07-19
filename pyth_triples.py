"""Contains functions for generating pythagorean triplets."""


def _mA(a, b, c):
    return ( a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c)
def _mB(a, b, c):
    return ( a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c)
def _mC(a, b, c):
    return (-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)
def prim_pyth_triples_dfs(start=(3,4,5), max_perim=None):
    """Generates primitive pythagorean triplets with perimeter at most
    max_perim by depth-first-search in a tree, see
    https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples"""
    if max_perim is None:
        raise Exception("max_perim must be given")
    a, b, c = start
    if a + b + c > max_perim:
        return
    
    yield start
    yield from prim_pyth_triples_dfs(_mA(a, b, c), max_perim=max_perim)
    yield from prim_pyth_triples_dfs(_mB(a, b, c), max_perim=max_perim)
    yield from prim_pyth_triples_dfs(_mC(a, b, c), max_perim=max_perim)
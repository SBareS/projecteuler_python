"""Contains some functions for dealing with directed graphs, implemented
as dictionaries assigning to each vertex a list of HalfEdge-objects, 
which simply encodes the other vertex of the edge (but, throug 
inheritance, might encode additional information). Vertices can be any
hashable objects, except None which has a special meaning in some 
functions."""

from heapq import heapify, heappop, heappush
from math import inf

from typing import Any

class HalfEdge:
    def __init__(self, end) -> None:
        self.end = end

class WeightedHalfEdge(HalfEdge):
    def __init__(self, end, weight) -> None:
        super().__init__(end)
        self.weight = weight

def dijkstra(G : dict[Any, list[WeightedHalfEdge]], source, goal=None):
    """Computes the shortest-distance tree rooted at source. G should be
    a weighted graph, i.e. the edges should be of type WeightedEdge. The
    result is a tuple of two dictionaries (dist, prev) associating to 
    each vertex its shortest distance to source, and the previous 
    vertex along that path. If the argument goal is set to something 
    other than None, the full tree might not be computed - only enough 
    to establish the shortest path from source to goal."""
    dist = {v: inf for v in G}
    dist[source] = 0
    prev = {v: None for v in G}
    
    visited = set()

    # Break ties in the pqueue with the insertion order so as to avoid
    # having to compare the vertices
    queue = [(dist[v], i, v) for i, v in enumerate(G)]
    next_tiebreak = len(queue)
    heapify(queue)

    while queue:
        du, _, u = heappop(queue)
        if u in visited:
            # Remnant in the queue, skip
            continue
        if goal is not None and u == goal:
            # Yay, we found the goal!
            break
        if du == inf:
            # u is not reachable, so neither is any later vertices in
            # the queue
            break
        visited.add(u)
        
        for edge in G[u]:
            v = edge.end
            if v in visited:
                continue
            new_dist = du + edge.weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heappush(queue, (new_dist, next_tiebreak, v))
                next_tiebreak += 1
    
    return dist, prev
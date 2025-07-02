class UnionFind:
    
    def __init__(self, join_data = None):
        """Constructor for the UnionFind class. The sets can be augmented with
        some extra data by supplying the optional parameter join_data, which
        should be a function for combining the data of two sets during union
        operations. For example, augmenting all nodes with the integer 1 on 
        creation and using join_data=operator.add will augment the sets with 
        their cardinality."""
        self.parent = {}
        self.rank = {}
        self.data = {}
        if join_data is not None:
            self._join_data = join_data
        
    def add_node(self, key, data=None):
        self.parent[key] = key
        self.rank[key] = 0
        if data is not None:
            self.data[key] = data
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        rx = self.rank[x]
        ry = self.rank[y]
        
        if rx < ry:
            x, rx, y, ry = y, ry, x, rx
        self.parent[y] = x
        if rx == ry:
            self.rank[x] = rx + 1
        
        if x in self.data or y in self.data:
            self.data[x] = self._join_data(self.data[x], self.data[y])
            del self.data[y] # Not strictly necessary, but it frees a bit of memory
    
    def find(self, x):
        while (p := self.parent[x]) != x:
            pp = self.parent[p]
            self.parent[x] = self.parent[p] = x = pp
        return x

    def get_data(self, x):
        return self.data[self.find(x)]
    
    def _join_data(self, d1, d2):
        raise NotImplementedError(
            "join_data should be supplied in the UnionFind constructor, if " \
            "augmenting sets with data.")
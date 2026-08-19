class UnionFind:
    def __init__(self, parent, size):
        self.parent = parent
        self.size = size

    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        x = self.find(x); y = self.find(y)
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
            self.size[y] = self.size[x]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            self.size[x] = self.size[y]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {i:set() for i in range(1, len(edges) + 1)}
        for a,b in edges:
            graph[a].add(b); graph[b].add(a)

        for a,b in edges[::-1]:
            graph[a].remove(b)
            graph[b].remove(a)
            parent = [i for i in range(len(edges) + 1)]
            size = [1] * (len(edges) + 1)
            uf = UnionFind(parent, size)
            for node in graph:
                for neighbor in graph[node]:
                    uf.union(node, neighbor)
        
            parent_set = set(uf.find(i) for i in range(1, len(edges) + 1))
            if len(parent_set) == 1:
                return [a,b]
            
            graph[a].add(b); graph[b].add(a)

        
        return []

        


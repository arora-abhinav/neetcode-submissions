class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N + 1)]
        size = [1] * (N + 1)

        def find(n):
            if parent[n] == n:
                return parent[n]
            parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2) -> bool:
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            
            else:
                parent[p1] = p2
                size[p2] += p1
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

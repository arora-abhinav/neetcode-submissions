class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:set() for i in range(n)}
        for a, b in edges:
            graph[a].add(b); graph[b].add(a);

        parent = [i for i in range(n)]
        size = [1] * n

        def find(node):
            if parent[node] == node:
                return node 
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(x, y):
            if size[x] > size[y]:
                parent[find(y)] = find(x)
                size[x] += size[y]
                size[y] = size[x]
            else:
                parent[find(x)] = find(y)
                size[y] += size[x]
                size[x] = size[y]
        
        for node in graph:
            for neighbor in graph[node]:
                union(node, neighbor)
        
        count = 0
        for (index, p) in enumerate(parent):
            if index == p:
                count += 1
        
        return count 
        
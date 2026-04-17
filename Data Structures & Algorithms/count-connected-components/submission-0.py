class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        counter = 0
        adj = {i:[] for i in range(n)}
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)

        visited = set()
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        for node in adj:
            if node not in visited:
                dfs(node)
                counter += 1
        
        return counter
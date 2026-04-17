class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}
        for node, pointer in edges:
            #Bidirectional Edge
            adj[node].append(pointer)
            adj[pointer].append(node)
        
        visited = set()
        def cycle(node, prev):

            if node in visited:
                return False
            
            visited.add(node)
            for n in adj[node]:
                if n != prev and not cycle(n, node):
                    return False
            
            return True
        
        
        return cycle(0, -1) and len(visited) == n

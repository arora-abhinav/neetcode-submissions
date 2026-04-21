from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
        
        processed = 0
        visited = set()
        def bfs(start):
            q = deque()
            q.append(start)

            while q:
                qLen = len(q)
                for _ in range(qLen):
                    node = q.popleft()
                    visited.add(node)
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            q.append(neighbour)
            
        for node in graph:
            if node not in visited:
                bfs(node)
                processed += 1
        
        return processed
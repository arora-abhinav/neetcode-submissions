from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:set() for i in range(n)}; q = deque()
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        if n - 1 != len(edges):
            return False
        
        q.append(0); visited = set(); processed = 0;
        visited.add(0)
        while q:
            qLen = len(q)
            for _ in range(qLen):
                popped = q.popleft()
                processed += 1
                for neighbor in graph[popped]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        return True if processed == n else False

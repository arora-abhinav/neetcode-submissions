class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        edge_count = 0
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
            edge_count += 1
        
        if edge_count != n - 1:
            return False
        processed = 0
        visited = set()
        def bfs():
            nonlocal processed
            q = deque()
            q.append(0)

            while q:
                qLen = len(q)
                for _ in range(qLen):
                    node = q.popleft()
                    visited.add(node)
                    processed += 1
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            q.append(neighbour)
        
        bfs()
        return processed == n
            

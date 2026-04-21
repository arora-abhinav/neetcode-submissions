import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, dest, weight in times:
            graph[source].append((dest, weight))
        
        print(graph)
        dist = {}
        visited = set()

        heap = [(0, k)]
        heapq.heapify(heap)
        while heap:
            d, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            dist[node] = d
            visited.add(node)
            
            for neighbour, n_dist in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(heap, (d + n_dist, neighbour))
        
        return max(dist.values()) if len(dist) == n else -1
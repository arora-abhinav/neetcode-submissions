import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:set() for i in range(1, n + 1)}
        for u,v,t in times:
            graph[u].add((v, t))
        
        heap = []; visited = set();
        heapq.heapify(heap)
        heapq.heappush(heap, (0,k))
        times = [float('inf') for i in range(n + 1)]
        while heap:
            popped = heapq.heappop(heap)
            time, node = popped[0], popped[1]
            if node not in visited:
                visited.add(node)
                times[node] = min(times[node], time)
                for neighbor, n_time in graph[node]:
                    heapq.heappush(heap, (time + n_time, neighbor))
        
        return max(times[1:]) if len(visited) == n else -1
        


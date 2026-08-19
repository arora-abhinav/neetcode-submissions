import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i:set() for i in range(len(points))}
        def manhattan_dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]; x2,y2 = points[j]
                m = manhattan_dist(x1, y1, x2, y2)
                graph[i].add((j, m))
                graph[j].add((i, m))
        
        res = 0
        heap = [(0, 0)]; heapq.heapify(heap); visited = set()
        while heap:
            dist, point = heapq.heappop(heap)
            if point not in visited:
                visited.add(point)
                res += dist
                for neighbor in graph[point]:
                    p, d = neighbor;
                    if p in visited:
                        continue
                    heapq.heappush(heap, (d, p))
        
        return res
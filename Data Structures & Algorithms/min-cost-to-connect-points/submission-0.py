import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0

        minHeap = [[0, 0]]
        while len(visited) != len(points):
            dist, ind = heapq.heappop(minHeap)
            print(dist)
            if ind in visited:
                continue
            
            res += dist

            visited.add(ind)

            for point in adj[ind]:
                if point[1] not in visited:
                    heapq.heappush(minHeap, [point[0], point[1]])
            
        return res


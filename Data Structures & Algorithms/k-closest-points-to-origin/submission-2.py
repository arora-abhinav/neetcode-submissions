import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_map = []
        heapq.heapify(point_map)
        for point in points:
            x, y = point
            heapq.heappush(point_map, ((x,y), math.sqrt(x**2 + y**2)))

        res = heapq.nsmallest(k, point_map, key = lambda item:item[1])
        new = []
        for mapping in res:
            point, dist = mapping
            x,y = point
            new.append([x, y])
        
        return new



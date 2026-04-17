import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        heapq.heapify_max(heap)
        for i in points:
            dist = (i[0]**2 + i[1]**2)**0.5
            if len(heap) < k:
                heapq.heappush_max(heap, (dist, i))

            elif len(heap) == k:
                largest = heap[0]
                if dist < largest[0]:
                    elt = heapq.heappop_max(heap)
                    heapq.heappush_max(heap,(dist, i))
            
        for i in heap:
            res.append(i[-1])
        
        return res
        
        

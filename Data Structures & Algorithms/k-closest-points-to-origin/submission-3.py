class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for ind, p in enumerate(points):
            dist = ((p[0])**2 + p[1]**2)**0.5
            res.append((dist, ind))
        
        heapq.heapify_max(res)
        while len(res) > k:
            heapq.heappop_max(res)
        
        final = []
        for dist, ind in res:
            print(ind)
            final.append(points[ind])
        
        return final
        
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while len(heap) > 1:
            heaviest = heapq.nlargest(2, heap)
            b = heaviest[0]
            s = heaviest[-1]

            if b == s:
                heapq.heappop_max(heap)
                heapq.heappop_max(heap)
            
            elif b > s:
                elt_1 = heapq.heappop_max(heap)
                elt_2 = heapq.heappop_max(heap)
                res = elt_1 - elt_2
                heapq.heappush_max(heap, res)

        if len(heap) == 1:
            return heap[0]
        return 0
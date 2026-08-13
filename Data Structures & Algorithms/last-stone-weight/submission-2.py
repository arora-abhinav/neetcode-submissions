import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            res = abs(a - b)
            if res > 0:
                heapq.heappush_max(stones, res)

        return stones[-1] if len(stones) > 0 else 0 
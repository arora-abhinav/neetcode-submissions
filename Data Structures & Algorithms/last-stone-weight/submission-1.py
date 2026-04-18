class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            res = heapq.nlargest(2, stones)
            heapq.heappop_max(stones)
            heapq.heappop_max(stones)
            if res[0] != res[1]:
                new = max(res[0], res[1]) - min(res[0], res[1])
                heapq.heappush_max(stones, new)
        
        if len(stones) != 0:
            return stones[0]
        return 0



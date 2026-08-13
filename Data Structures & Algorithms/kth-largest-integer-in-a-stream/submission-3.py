import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify_max(self.heap)
        for num in nums:
            heapq.heappush_max(self.heap, num)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        res = heapq.nlargest(self.k, self.heap)
        return res[-1]

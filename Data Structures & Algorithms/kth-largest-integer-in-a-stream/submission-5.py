import heapq
class KthLargest:

    def helper(self, heap, k, number):
        heapq.heappush(heap, number)
        if len(heap) > k:
            heapq.heappop(heap)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)
        for num in nums:
            self.helper(self.heap, self.k, num)

    def add(self, val: int) -> int:
        self.helper(self.heap, self.k, val)
        return self.heap[0]

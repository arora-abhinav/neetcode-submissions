import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.main_heap = nums
        self.n = k
        heapq.heapify_max(self.main_heap)
        print(self.main_heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.main_heap, val)
        return heapq.nlargest(self.n, self.main_heap)[-1]

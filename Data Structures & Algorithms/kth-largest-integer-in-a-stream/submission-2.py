import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.num = 0 
        heapq.heapify_max(self.heap)
        for i in range(len(nums)):
            heapq.heappush_max(self.heap, nums[i])
        self.num = k
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        return heapq.nlargest(self.num, self.heap)[-1]
        

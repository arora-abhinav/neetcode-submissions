import heapq
import math
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify_max(self.max_heap)
        self.median = 0

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max_heap, num)
        if self.max_heap and self.min_heap and self.max_heap[0] > self.min_heap[0]:
            elt = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, elt)
        if len(self.max_heap) - len(self.min_heap) == 2:
            elt = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, elt)
        if len(self.min_heap) - len(self.max_heap) == 2:
            elt = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, elt)
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0])/2
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        return self.min_heap[0]
        
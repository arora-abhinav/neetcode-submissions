import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []; self.max_heap = [];
        heapq.heapify(self.min_heap); heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max_heap, num)
        if self.min_heap and self.max_heap and self.max_heap[0] > self.min_heap[0]:
            popped = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, popped)

        if len(self.max_heap) - len(self.min_heap) > 1:
            popped = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, popped)

        if len(self.min_heap) - len(self.max_heap) > 1:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, popped)

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + self.max_heap[0])/2
        return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else self.max_heap[0]
        
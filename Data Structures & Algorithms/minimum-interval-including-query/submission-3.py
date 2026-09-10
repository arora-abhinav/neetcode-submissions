import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []; heapq.heapify(heap);
        res = [-1] * len(queries); 
        #Sorting queries based on value but preserving their index
        queries = sorted(enumerate(queries), key = lambda x:x[1])
        intervals.sort(); a = 0
        for index, i in queries:
            while a < len(intervals) and intervals[a][0] <= i:
                heapq.heappush(heap, (intervals[a][1] - intervals[a][0] + 1, intervals[a][1]))
                a += 1
            while heap and heap[0][1] < i:
                heapq.heappop(heap)
            if heap:
                res[index] = heap[0][0]
        
        return res
        
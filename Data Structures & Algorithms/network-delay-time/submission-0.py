import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        m = {i: [] for i in range(1, n + 1)}
        for ui, vi, ti in times:
            m[ui].append([vi, ti])
        
        shortest = {}
        minHeap = [[0, k]]
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in m[n1]:
                if n2 not in shortest:

                    heapq.heappush(minHeap, [w1 + w2, n2])
        

        if len(shortest) != n:
            return -1
            

        return max(shortest.values())
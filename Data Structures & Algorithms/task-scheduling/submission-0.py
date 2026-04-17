from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        heap = []
        frequency_map = {}
        time = 0
        heapq.heapify_max(heap)
        for i in tasks:
            if i not in frequency_map:
                frequency_map[i] = 1
            else:
                frequency_map [i] += 1
        
        for k in frequency_map.values():
            heapq.heappush_max(heap, k)
        
        while heap or q:
            time += 1
            if heap:
                elt = heapq.heappop_max(heap)
                elt -= 1
                if elt != 0:
                    q.append((elt, time + n))

            if q and time == q[0][1]:
                elt = q.popleft()
                heapq.heappush_max(heap, elt[0])
        
        print (heap)
        return time

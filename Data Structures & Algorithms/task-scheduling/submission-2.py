from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [i for i in counter.values()]
        remaining = sum(counter.values())
        heapq.heapify_max(heap)
        q = deque()
        time = 0
        final = 0
        while remaining > 0:
            if q:
                if q[0][1] == time:
                    l = q.popleft()
                    heapq.heappush_max(heap, l[0])
            
            if heap:
                l = heapq.heappop_max(heap)
                if l - 1 > 0:
                    q.append((l-1, time + n + 1))
                remaining -= 1
            
            time += 1
        
        return time

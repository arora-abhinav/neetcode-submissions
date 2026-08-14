from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0; to_process = 0;
        q = deque();
        task_counter = Counter(tasks); heap = [i for i in task_counter.values()];
        heapq.heapify_max(heap)
        to_process = sum(task_counter.values())
        while to_process > 0:
            if heap:
                popped = heapq.heappop_max(heap)
                to_process -= 1
                q.append((time + n, popped - 1))
            if q:
                if time == q[0][0]:
                    popped = q.popleft()
                    if popped[1] > 0:
                        heapq.heappush_max(heap, popped[1])
            time += 1
        
        return time
            

        
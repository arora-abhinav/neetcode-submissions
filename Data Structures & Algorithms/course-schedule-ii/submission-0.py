class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(numCourses)}; pre = {i:0 for i in range(numCourses)}

        for a,b in prerequisites:
            graph[b].add(a)
            pre[a] += 1
        
        q = deque(); count = len(pre)
        for course in pre:
            if pre[course] == 0:
                q.append(course)
        ordering = []; 
        while q:
            qLen = len(q)
            for _ in range(qLen):
                popped = q.popleft()
                ordering.append(popped)
                for course in graph[popped]:
                    pre[course] -= 1
                    if pre[course] == 0:
                        q.append(course)
        
        if len(ordering) != count:
            return []
        return ordering 



        
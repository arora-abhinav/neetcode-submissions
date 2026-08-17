from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}; pre_counter = defaultdict(int)
        for n, pre in prerequisites:
            if pre not in graph:
                graph[pre] = set()
            if n not in graph:
                graph[n] = set()
            pre_counter[n] += 1
            if pre not in pre_counter:
                pre_counter[pre] = 0
            graph[pre].add(n)

        q = deque()
        for course in pre_counter:
            if pre_counter[course] == 0:
                q.append(course)

        print(pre_counter)
        course_counter = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                popped = q.popleft()
                course_counter += 1
                for c in graph[popped]:
                    if pre_counter[c] == 0:
                        continue
                    pre_counter[c] -= 1
                    if pre_counter[c] == 0:
                        q.append(c)
        
        return course_counter == len(graph)




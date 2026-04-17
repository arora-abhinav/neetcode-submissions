class node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completed = set()
        courses = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        def dfs(course) -> bool:
            if courses[course] == []:
                return True
            
            if course in completed:
                return False
            
            completed.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False
            completed.remove(course)
            return True

        for course in courses:
            res = dfs(course)
            if not res:
                return False
        
        return True

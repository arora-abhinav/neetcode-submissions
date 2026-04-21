class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_s = {i:[] for i in range(numCourses)}
        visited = set()
        visiting = set()
        for course, pre in prerequisites:
            pre_s[course].append(pre)
        
        def dfs(node):
            if node in visited:
                return True
            
            if node in visiting:
                return False
            
            visiting.add(node)

            for neighbour in pre_s[node]:
                if not dfs(neighbour):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True 

        for course in pre_s:
            if not dfs(course):
                return False
        
        return True


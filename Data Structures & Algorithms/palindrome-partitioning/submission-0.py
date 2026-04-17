class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer, sol = [], []

        def dfs(ind):
            if ind == len(s):
                answer.append(sol.copy())
                return
            
            for j in range(ind, len(s)):
                if s[ind: j + 1] == s[ind: j + 1][::-1]:
                    sol.append(s[ind:j+1])
                    dfs(j + 1)
                    sol.pop()
        
        dfs(0)
        return answer
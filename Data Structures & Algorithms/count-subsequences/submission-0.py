from collections import defaultdict
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #i: index of s, k: index of t
        dp = {}
        for i in range(len(s)):
            for k in range(len(t)):
                dp[(i, k)] = float('-inf')
        def dfs(i, k, cur):
            if k >= len(t):
                print(True, cur)
                if cur == t:
                    return 1
                return 0
            if i >= len(s):
                return 0
            if (i, k) in dp and dp[(i, k)] != float('-inf'):
                return dp[(i, k)]
            
            dp[(i, k)] = 0
            if i < len(s) and s[i] == t[k]:
                dp[(i, k)] += dfs(i + 1, k + 1, cur + s[i]) + dfs(i + 1, k , cur)
            else:
                dp[(i, k)] += dfs(i + 1, k, cur)
            return dp[(i, k)]
        
        res = dfs(0, 0, "")
        return res

        
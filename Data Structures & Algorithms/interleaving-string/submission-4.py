class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #4 choices: continue adding str1, cut str1 and start adding str2, continue adding str2, cut str2 and start adding str1
        dp = {}
        def dfs(i, j, cur, k):
            if k >= len(s3):
                if cur == s3 and i >= len(s1) and j >= len(s2):
                    return True
                return False
            
            if (i, j, cur) in dp:
                return dp[(i, j, cur)]
            
            res1 = False; res2 = False
            if i < len(s1) and s3[k] == s1[i]:
                res1 = dfs(i + 1, j, cur + s1[i], k + 1)
            if j < len(s2) and s3[k] == s2[j]:
                res2 = dfs(i, j + 1, cur + s2[j], k + 1)
            dp[(i,j, cur)] = res2 or res1
            return dp[(i, j, cur)]
        

        res = dfs(0, 0, "", 0)
        return res
            
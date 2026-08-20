class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[None] * len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                dp[j- 1][j] = True
                count += 1
            else:
                dp[j - 1][j] = False
        
        def sol(i, j):
            nonlocal count
            while (0 <= i < len(s)) and (0 <= j < len(s)):
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    count += 1
                    dp[i][j] = True
                
                i += 1; j += 1
        
        for k in range(2, len(s)):
            sol(0, k)
        
        return count
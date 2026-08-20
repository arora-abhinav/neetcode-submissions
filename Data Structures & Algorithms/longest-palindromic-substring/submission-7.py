class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[None] * (len(s)) for _ in range(len(s))]
        maxlen = -float('inf'); substring = s[0]
        for i in range(len(s)):
            dp[i][i] = True
        for j in range(1,len(s)):
            if s[j - 1] == s[j]:
                dp[j - 1][j] = True
                maxlen = 2
                substring = s[j-1: j + 1]
            else:
                dp[j - 1][j] = False

        
        def dfs(i, j):
            nonlocal maxlen; nonlocal substring;
            while 0 <= i < len(s) and 0 <= j < len(s):
                if s[i] == s[j] and dp[i+1][j-1]:
                    if (j - i + 1) > maxlen:
                        substring = s[i: j + 1]
                        maxlen = j - i + 1
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                
                i += 1; j += 1
        
        for k in range(2, len(s)):
            dfs(0, k)
        
        return substring

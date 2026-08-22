class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-float('inf')] * n for _ in range(m)]
        for i in range(len(dp[0])):
            dp[-1][i] = 1
        for i in range(len(dp)):
            dp[i][-1] = 1
        print(dp)
        
        for row in range(len(dp) - 2, -1, -1):
            for col in range(len(dp[0]) - 2, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        
        return dp[0][0]

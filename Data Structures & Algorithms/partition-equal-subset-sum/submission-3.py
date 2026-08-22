class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = [[False for i in range(int(s/2) + 1)] for _ in range(len(nums) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                diff = j - nums[i - 1]
                if diff < 0:
                    dp[i][j] = dp[i-1][j]
                elif diff == 0:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][diff] or dp[i-1][j]
        
        return dp[-1][-1]

        
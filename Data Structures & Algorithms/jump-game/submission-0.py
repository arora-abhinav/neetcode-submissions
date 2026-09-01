class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums); dp[-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                continue
            if nums[i] + i >= len(nums) - 1:
                dp[i] = True
            else:
                for k in range(nums[i], -1, -1):
                    dp[i] = dp[i] or dp[i + k]
        
        return dp[0]
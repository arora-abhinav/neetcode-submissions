class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {i: float('inf') for i in range(len(nums))}; dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                dp[i] = 1
            else:
                for j in range(nums[i], -1, -1):
                    dp[i] = min(dp[i], 1 + dp[i + j])
        
        print(dp)
        return dp[0]

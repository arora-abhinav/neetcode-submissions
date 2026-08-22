class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            choices = [1]
            for j in range(i, len(nums) - 1):
                if nums[j + 1] > nums[i]:
                    choices.append(1 + dp[j + 1])
            dp[i] = max(choices)
        
        return max(dp)

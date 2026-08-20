class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [-float('inf')] * len(nums)
        max_sum = 0
        if len(nums) <= 2:
            return max(nums)
        def dp(i):
            if i >= len(robbed):
                return 0
            if robbed[i] != -float('inf'):
                return robbed[i]
            for j in range(2, len(robbed)):
                robbed[i] = max(robbed[i], nums[i] + dp(i + j))
            
            return robbed[i]
        
        for i in range(len(nums)):
            dp(i)
        return max(robbed)
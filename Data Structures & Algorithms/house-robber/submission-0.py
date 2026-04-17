class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = [-1] * len(nums)
        def dfs(i):
            if i > len(nums) - 1 or i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        
        return max(dfs(0), dfs(1))
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, cur):
            if i >= len(nums):
                if cur == target:
                    return 1
                return 0
            if (i, cur) in dp:
                return dp[(i, cur)]
            
            #Two choices: either add or subtract, but regardless move to the next element
            dp[(i, cur)] = dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])
            return dp[(i, cur)]
        
        return dfs(0, 0)
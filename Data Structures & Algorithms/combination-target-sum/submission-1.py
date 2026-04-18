class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(subset.copy())
                return
            if cur_sum > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            cur_sum += nums[i]
            dfs(i, cur_sum)
            subset.pop()
            cur_sum -= nums[i]
            dfs(i + 1, cur_sum)
        
        dfs(0, 0)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sums = []
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sums.copy())
                return
            if cur_sum > target or i >= len(nums):
                return
            
            cur_sum += nums[i]
            sums.append(nums[i])
            backtrack(i, cur_sum)
            cur_sum -= nums[i]
            sums.pop()
            backtrack(i+1, cur_sum)
        
        backtrack(0, 0)
        return res

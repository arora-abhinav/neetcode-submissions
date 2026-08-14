class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        c_sum = 0
        res, cur = [], []
        def dfs(i):
            nonlocal c_sum
            if c_sum == target:
                res.append(cur.copy())
                return
            if i > len(nums) - 1 or c_sum > target:
                return
            cur.append(nums[i])
            c_sum += nums[i]
            dfs(i)
            p = cur.pop()
            c_sum -= p
            dfs(i + 1)
            return
        
        dfs(0)
        return res
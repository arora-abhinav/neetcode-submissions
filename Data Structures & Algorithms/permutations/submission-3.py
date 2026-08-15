class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res, cur = [], []
        def dfs():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                cur.append(nums[i])
                used[i] = True
                dfs()
                cur.pop()
                used[i] = False
        
        dfs()
        return res
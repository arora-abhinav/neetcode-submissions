class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        perms = []

        def backtrack():
            if len(nums) == len(perms):
                res.append(perms.copy())
                return
        
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    backtrack()
                    perms.pop()
        
        backtrack()
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        l = len(nums)
        arr, sol = [], []

        def backTrack():
            if len(sol) == l:
                arr.append(sol.copy())
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    print(sol)
                    backTrack()
                    sol.pop()
        backTrack()
        return arr
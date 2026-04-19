class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sub, arr = [], []
        def backTrack():
            if len(sub) == len(nums):
                arr.append(sub.copy())
                return

            for x in nums:
                if x not in sub:
                    sub.append(x)
                    backTrack()
                    sub.pop()
        
        backTrack()
        return arr


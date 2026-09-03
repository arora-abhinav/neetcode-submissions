class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm
        s = 0; m = float('-inf')
        for n in nums:
            if s <= 0:
                s = n
            else:
                s += n
            m = max(m, s)
        return m
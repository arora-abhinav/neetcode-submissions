class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n**2 + n)/2
        for num in nums:
            s -= num
        return int(s)
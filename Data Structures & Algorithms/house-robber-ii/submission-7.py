class sol:
    def __init__(self, arr):
        self.arr = arr
        self.memo = [float('-inf')] * len(arr)
    
    def dp(self, i):
        if i >= len(self.arr):
            return 0
        if self.memo[i] != float('-inf'):
            return self.memo[i]
        self.memo[i] = max(self.dp(i + 1), self.arr[i] + self.dp(i + 2))
        return self.memo[i]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        arr1 = nums[1:]; arr2 = nums[:-1]
        sol1 = sol(arr1); sol2 = sol(arr2)
        sol1.dp(0); sol2.dp(0); m1 = max(sol1.memo); m2 = max(sol2.memo)
        return max(m1, m2)


        
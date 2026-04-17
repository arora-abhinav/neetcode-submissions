class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        c2 = [-1] * (N - 1)
        c3 = [-1] * (N - 1)
        def dfs(i, arr, cache):
            if i < 0 or i > N - 2:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(dfs(i + 1, arr, cache), arr[i] + dfs(i + 2, arr, cache))
            return cache[i]
        
        return max(dfs(0, nums[:-1], c2), dfs(0, nums[1:], c3))
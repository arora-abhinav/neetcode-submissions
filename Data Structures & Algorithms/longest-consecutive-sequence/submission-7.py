class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        visited = set()
        max_len = 0
        def dfs(num):
            if num in visited or num not in n:
                return 0
            visited.add(num)
            return 1 + dfs(num + 1)
        
        for num in nums:
            if num -1 not in n:
                max_len = max(max_len, dfs(num))
        
        return max_len
                


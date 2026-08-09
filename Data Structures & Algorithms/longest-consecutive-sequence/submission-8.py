class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starts = []

        for num in num_set:
            if num - 1 not in num_set:
                starts.append([num])
        
        for s in starts:
            n = s[0]
            while n + 1 in num_set:
                s.append(n + 1)
                n += 1

        max_len = 0
        for s in starts:
            max_len = max(max_len, len(s))

        return max_len
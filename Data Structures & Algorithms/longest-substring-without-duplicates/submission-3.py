class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        m = 0
        chars = set()
        while end < len(s):
            while s[end] in chars:
                chars.remove(s[start])
                start += 1
            chars.add(s[end])
            m = max(m, end-start+1)
            end += 1
        return m
        # vzabcdavvbugu
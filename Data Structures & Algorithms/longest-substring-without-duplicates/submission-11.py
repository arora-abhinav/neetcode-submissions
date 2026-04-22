class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        j = 0
        visited = set()
        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                res = max(res, j - i + 1)
                j += 1
            else:
                visited.remove(s[i])
                i += 1
            
        
        return res
            
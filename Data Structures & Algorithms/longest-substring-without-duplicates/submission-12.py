class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0, 0
        max_len = 0
        string_set = set()
        while j < len(s):
            while j < len(s) and s[j] not in string_set:
                string_set.add(s[j])
                j += 1
            max_len = max(max_len, len(string_set))
            string_set.remove(s[i])
            i += 1
        
        return max_len
            
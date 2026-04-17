class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        if not s:
            return 0
        substring = s[i]
        current_substring = s[i]
        last_seen = {}
        last_seen[s[i]] = i
        while j < len(s):
            if s[j] in last_seen and last_seen[s[j]] >= i:
                i = last_seen[s[j]] + 1
            last_seen[s[j]] = j
            current_substring = s[i:j+1]
            if len(current_substring) > len(substring):
                substring = current_substring
            j += 1
        
        return len(substring)
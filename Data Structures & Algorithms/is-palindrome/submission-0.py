class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        while start < end:
            
            if s[start].isalnum() and s[end].isalnum():
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1
        return True

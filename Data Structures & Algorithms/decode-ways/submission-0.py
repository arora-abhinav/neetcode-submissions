class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        
        def dfs(i):  # i = current position in string
            nonlocal count
            if i == len(s):  # reached the end successfully
                count += 1
                return
            if s[i] == '0':  # can't decode a leading zero
                return
            
            # Try taking 1 digit
            dfs(i + 1)
            
            # Try taking 2 digits if valid
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                dfs(i + 2)
        
        dfs(0)
        return count
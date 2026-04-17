class Solution:
    def countSubstrings(self, s: str) -> int:
        arr = []
        def dfs(i, string):
            
            if string and string == string[::-1]:
                arr.append(string)
            
            if i < len(s)- 1:
                dfs(i + 1, string + s[i + 1])
        
        for i in range(len(s)):
            dfs(i, s[i])
        
        print(arr)
        return len(arr)
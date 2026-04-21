class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        strings = []
        def backtrack(i):
            if len("".join(strings)) == len(s):
                res.append(strings.copy())
                return
            
            if i >= len(s):
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    strings.append(s[i:j+1])
                    backtrack(j+1)
                    strings.pop()
            
        backtrack(0)
        return res
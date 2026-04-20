class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        string = []
        def backtrack(i):
            if i >= len(s):
                res.append(string.copy())
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    string.append(s[i:j+1])
                    backtrack(j+1)
                    string.pop()

        backtrack(0)
        return res  



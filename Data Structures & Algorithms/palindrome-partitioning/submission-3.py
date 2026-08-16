class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []; cur = [];
        def dfs(start, end):
            if end == len(s):
                if start == end:
                    res.append(cur.copy())
                return
            
            #Keeping the current letter
            dfs(start, end + 1)
            #Splitting the substring
            substring = s[start: end + 1]
            if substring == substring[::-1]:
                cur.append(substring[::])
                dfs(end + 1, end + 1)
                cur.pop()
        
        dfs(0, 0)
        return res

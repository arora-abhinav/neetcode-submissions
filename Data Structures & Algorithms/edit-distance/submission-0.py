class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #3 choices: delete, replace, insert (insert the same character if it isn't equal)

        dp = {}
        def dfs(i, k, cur):
            if k >= len(word2) and i < len(word1):
                return len(word1) - i
            if i >= len(word1) and k < len(word2):
                return len(word2) - k
            if i >= len(word1) and k>= len(word2):
                return 0
            
            if (i, k) in dp:
                return dp[(i, k)]
            
            operations = float('inf')
            if i < len(word1) and word1[i] == word2[k]:
                operations = min(operations, dfs(i + 1, k + 1, cur + word1[i]))
            else:
                delete = dfs(i + 1, k, cur)
                replace = dfs(i + 1, k + 1, cur + word2[k])
                insert = dfs(i, k + 1, cur + word2[k])
                operations = min(operations, 1 + delete, 1 + replace, 1 + insert)
            dp[(i, k)] = operations
            return operations
        
        res = dfs(0, 0, "")
        return res
                

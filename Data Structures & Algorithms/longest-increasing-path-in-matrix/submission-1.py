from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #Move up, move left, move right, move down
        dp = defaultdict(int)
        def dfs(r, c, prev):
            if not (0 <= r < len(matrix)) or not (0 <= c < len(matrix[0])):
                return 0
            
            if (r, c, prev) in dp and dp[(r, c, prev)] != float('-inf'):
                return dp[(r, c, prev)]
            
            condition = matrix[r][c] > prev
            if condition:
                left = dfs(r , c - 1, matrix[r][c])
                right = dfs(r, c + 1, matrix[r][c])
                up = dfs(r - 1, c, matrix[r][c])
                down = dfs(r + 1, c, matrix[r][c])
                dp[(r,c, prev)] = max(1 + left, 1 + right, 1 + down, 1 + up)
            
            return dp[(r, c, prev)]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, float('-inf'))
        
        return max(dp.values())
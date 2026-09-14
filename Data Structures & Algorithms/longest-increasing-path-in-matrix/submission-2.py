from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #Move up, move left, move right, move down
        dp = defaultdict(int)
        def dfs(r, c, prev):
            if not (0 <= r < len(matrix)) or not (0 <= c < len(matrix[0])) or prev >= matrix[r][c]:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            left = dfs(r , c - 1, matrix[r][c])
            right = dfs(r, c + 1, matrix[r][c])
            up = dfs(r - 1, c, matrix[r][c])
            down = dfs(r + 1, c, matrix[r][c])
            dp[(r,c)] = max(1 + left, 1 + right, 1 + down, 1 + up)
            
            return dp[(r, c)]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, float('-inf'))
        
        return max(dp.values())
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set(); res = 0; cur = 0;
        def dfs(row, col):
            nonlocal cur
            if (row, col) in visited or not (0 <= row < len(grid)) or not(0 <= col < len(grid[0])) or grid[row][col] == 0:
                return
            
            visited.add((row, col))
            if grid[row][col] == 1: 
                cur += 1;
            dfs(row + 1, col); dfs(row - 1, col); dfs(row, col + 1); dfs(row, col -1);
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    cur = 0; dfs(row, col); res = max(res, cur)
        
        return res
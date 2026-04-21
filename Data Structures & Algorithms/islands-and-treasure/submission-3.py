class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(row, col, dist):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or dist > grid[row][col] or grid[row][col] == -1:
                return
            grid[row][col] = dist

            
            dfs(row + 1, col, dist + 1)
            dfs(row - 1, col, dist + 1)
            dfs(row, col + 1, dist + 1)
            dfs(row, col - 1, dist + 1)

        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        

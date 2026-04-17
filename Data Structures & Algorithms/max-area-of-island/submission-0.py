class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        cur = 0
        visited = set()
        def dfs(row, col):
            nonlocal cur
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or (row, col) in visited or grid[row][col] == 0:
                return
                
            cur += 1
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col)
                area = max(area, cur)
                cur = 0
        
        return area
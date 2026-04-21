class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_area = 0
        current_area = 0
        def dfs(row, col):
            nonlocal current_area
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 0:
                return 
            
            if grid[row][col] == 1:
                current_area += 1
            
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    current_area = 0
                    dfs(row, col)
                    max_area = max(max_area, current_area)
        
        return max_area
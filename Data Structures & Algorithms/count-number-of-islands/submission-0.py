from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(row, col):
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or (row, col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row, col))
            dfs(row + 1, col)
            visited.add((row, col))
            dfs(row - 1, col)
            visited.add((row, col))
            dfs(row, col + 1)
            visited.add((row, col))
            dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands
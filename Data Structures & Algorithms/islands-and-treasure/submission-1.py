class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(row, col, num):
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] < num or grid[row][col] == -1:
                return

            grid[row][col] = num

            dfs(row + 1, col, num + 1)
            dfs(row  - 1, col, num + 1)
            dfs(row, col + 1, num +1)
            dfs(row, col - 1, num + 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
         
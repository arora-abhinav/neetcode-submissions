class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        def dfs(row, col, visited, prev_height):
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or (row, col) in visited or prev_height > heights[row][col]:
                return
            
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        for col in range(len(heights[0])):
            dfs(0, col, pacific, float('-inf'))
            dfs(len(heights) - 1, col, atlantic, float('-inf'))
        
        for row in range(len(heights)):
            dfs(row, 0, pacific, float('-inf'))
            dfs(row, len(heights[0]) - 1, atlantic, float('-inf'))
        
        return [list(x) for x in pacific.intersection(atlantic)]
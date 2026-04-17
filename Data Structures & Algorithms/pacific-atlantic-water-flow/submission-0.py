class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        out = []
        pacific = set()
        atlantic = set()
        def dfs(row, col, s, prev):
            if row < 0 or col < 0 or row > len(heights) - 1 or col > len(heights[0]) - 1 or (row, col) in s or heights[row][col] < prev:
                return
            
            s.add((row, col))
            dfs(row + 1, col, s, heights[row][col])
            dfs(row - 1, col, s, heights[row][col])
            dfs(row, col + 1, s, heights[row][col])
            dfs(row, col - 1, s, heights[row][col])
        
        for row in range(len(heights)):
            dfs(row, 0, pacific, 0)
            dfs(row, len(heights[0]) - 1, atlantic, 0)
        
        for col in range(len(heights[0])):
            dfs(0, col, pacific, 0)
            dfs(len(heights) - 1, col, atlantic, 0)
        
        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res


            

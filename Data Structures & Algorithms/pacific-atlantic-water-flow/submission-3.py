class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(row, col, prev, visited):

            if not(0 <= row < len(heights)) or not (0 <= col < len(heights[0])) or (row, col) in visited or heights[row][col] < prev:
                return
            
            cur = heights[row][col]
            visited.add((row, col));
            dfs(row + 1, col, cur, visited); dfs(row -1, col, cur, visited); dfs(row, col + 1, cur, visited); dfs(row, col - 1, cur, visited)
    
        atlantic_flow = set(); pacific_flow = set(); res = set()
        for col in range(len(heights[0])):
            dfs(0, col, -float('inf'), pacific_flow); 
            dfs(len(heights)-1, col, -float('inf'), atlantic_flow);
        
        for row in range(len(heights)):
            dfs(row, 0, -float('inf'), pacific_flow); 
            dfs(row, len(heights[0]) - 1, -float('inf'), atlantic_flow);
        
        res = atlantic_flow.intersection(pacific_flow)
        final = []
        for x,y in res:
            arr = [x, y]
            final.append(arr)
        
        return final

            
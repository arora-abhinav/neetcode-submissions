from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs(q, visited:set):
            depth = 0
            while q:
                qLen = len(q)
                for i in range(qLen):
                    popped = q.popleft()
                    r,c = popped
                    if grid[r][c] > 0:
                        grid[r][c] = min(grid[r][c], depth)
                    dirs = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                    for d in dirs:
                        r, c = d
                        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] <= 0 or (r,c) in visited:
                            continue
                        q.append((r, c))
                        visited.add((r,c))
                depth += 1
        
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        bfs(q, set())
        print(grid)
                        
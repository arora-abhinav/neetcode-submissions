from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(q):
            visited = set()
            changed = 0; time = 0;
            while q:
                qLen = len(q)
                for i in range(qLen):
                    r,c = q.popleft()
                    if grid[r][c] != 2:
                        grid[r][c] = 2
                        changed += 1
                    dirs = ((r + 1,c), (r-1, c), (r, c+ 1), (r, c-1))
                    for d in dirs:
                        r,c = d
                        if not (0 <= c < len(grid[0])) or not (0 <= r < len(grid)) or  grid[r][c] == 0 or grid[r][c] == 2 or (r,c) in visited:
                            continue
                        q.append((r,c))
                        visited.add((r,c))
                if q:
                    time += 1
            return changed, time
        
        count = 0; q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        print(count)
        res, time = bfs(q)
        print(time)
        return -1 if res!=count else time

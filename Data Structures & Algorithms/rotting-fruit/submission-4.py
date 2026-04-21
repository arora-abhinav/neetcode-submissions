from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        while q and fresh > 0:
            qLen = len(q)
            for i in range(len(q)):
                row, col = q.popleft()
                coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for r, c in coordinates:
                    if 0 <= row + r < len(grid) and 0 <= col + c < len(grid[0]):
                        if grid[row + r][col + c] == 1:
                            q.append((row + r, col + c))
                            grid[row + r][col +c] = 2
                            fresh -= 1
            
            time += 1
        
        print(time)
        return time if fresh == 0 else -1

            
        
        
            
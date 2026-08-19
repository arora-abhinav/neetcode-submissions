import heapq
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        graph = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for d in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    r, c = d;
                    if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
                        continue 
                    if (row, col) not in graph:
                        graph[(row, col)] = set()
                    if (r, c) not in graph:
                        graph[(r,c)] = set()
                    graph[(row, col)].add((r,c))
                    graph[(r, c)].add((row, col))
        
        heap = [(grid[0][0], (0, 0))]; heapq.heapify(heap); visited = set();
        time = 0; 
        while heap:
            popped = heapq.heappop(heap)
            val, coords = popped; 
            time = max(time, val)
            if coords == (len(grid) - 1, len(grid[0]) - 1):
                return time
            if coords not in visited:
                visited.add(coords)
                for neighbor in graph[coords]:
                    if neighbor not in visited:
                        r,c = neighbor
                        heapq.heappush(heap, (grid[r][c], neighbor))
        
        return time

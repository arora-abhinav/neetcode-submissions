class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        orders = min(len(matrix), len(matrix[0]))//2
        row = len(matrix); col = len(matrix[0])
        res = []; visited = set()
        for i in range(orders + 1):
            #Top:
            for t in range(i, col - i):
                if (i, t) not in visited:
                    res.append(matrix[i][t])
                    visited.add((i, t))
            
            #Right:
            for r in range(i + 1, row - i - 1):
                if (r, col - 1 - i) not in visited:
                    res.append(matrix[r][col - i - 1])
                    visited.add((r, col - 1 - i) )
            
            #Bottom:
            for b in range(col - i - 1, i - 1, -1):
                if (row - i - 1, b) not in visited:
                    res.append(matrix[row - i - 1][b])
                    visited.add((row - i - 1, b))
            
            #left:
            for l in range(row - i - 1, i, -1):
                if (l, i) not in visited:
                    res.append(matrix[l][i])
                    visited.add((l, i))
        
        return res
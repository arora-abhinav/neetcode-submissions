from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #Anything thats on the border and connected in an "island" is NOT surrounded
        def bfs(q):
            processed = set()
            visited = set()
            while q:
                qLen = len(q)
                for i in range(qLen):
                    r,c = q.popleft()
                    if board[r][c] == "O":
                        board[r][c] = "N"
                    processed.add((r,c))
                    dirs = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                    for d in dirs:
                        r,c = d
                        if not (0 <= r < len(board)) or not(0 <= c < len(board[0])) or board[r][c] == "X" or board[r][c] == "N" or (r,c) in visited:
                            continue
                        visited.add ((r,c))
                        q.append((r,c))
        
        q = deque()
        for row in range(len(board)):
            if board[row][0] == "O":
                q.append((row, 0))
            if board[row][len(board[0])-1] == "O":
                q.append((row, len(board[0]) - 1))
        
        for col in range(len(board[0])):
            if board[0][col] == "O":
                q.append((0, col))
            if board[len(board) - 1][col] == "O":
                q.append((len(board) - 1, col))
        
        bfs(q)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "N":
                    board[row][col] = "O"
        

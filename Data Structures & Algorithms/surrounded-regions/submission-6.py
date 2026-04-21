from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "U"
        
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            board[row][col] = "O"
            while q:
                qLen = len(q)
                for i in range(len(q)):
                    row, col = q.popleft()
                    dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]
                    for r,c in dirs:
                        if 0 <= row + r < len(board) and 0 <= col + c < len(board[0]) and board[row + r][col + c] == "U":
                            print("Yes")
                            board[row + r][col + c] = "O"
                            q.append((row + r, col + c))

        for col in range(len(board[0])):
            if board[0][col] == "U":
                bfs(0, col)
            if board[len(board) - 1][col] == "U":
                bfs(len(board) - 1, col)
        for row in range(len(board)):
            if board[row][0] == "U":
                bfs(row, 0)
            if board[row][len(board[0]) - 1] == "U":
                bfs(row, len(board[0]) - 1)
            
        print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "U":
                    board[i][j] = "X"
        


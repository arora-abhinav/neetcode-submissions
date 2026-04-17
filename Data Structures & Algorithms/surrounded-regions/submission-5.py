class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or (row, col) in visited or board[row][col] != "O":
                return
            
            board[row][col] = "B"
            
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][len(board[0]) - 1] == "O":
                dfs(row, len(board[0]) - 1)
        
        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(0, col)
            if board[len(board) - 1][col] == "O":
                dfs(len(board) - 1, col)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "B":
                    board[r][c] = "O"
        


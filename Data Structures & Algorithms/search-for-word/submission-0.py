class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row, col, ind) -> bool:

            if len(word) == ind:
                return True
            
            if row > len(board) - 1 or row < 0 or col > len(board[0]) - 1 or col < 0 or board[row][col] != word[ind] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            res = dfs(row + 1, col, ind + 1) or dfs(row - 1, col, ind + 1) or dfs(row, col + 1, ind + 1) or dfs(row, col - 1, ind + 1)
            visited.remove((row, col))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False
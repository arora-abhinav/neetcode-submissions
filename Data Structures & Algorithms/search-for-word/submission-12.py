class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        word_arr = [i for i in word]
        visited = set(); final = False; arr = [];
        def dfs(row, col):
            nonlocal final
            if word_arr == arr:
                final = True
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or (row, col) in visited or len(arr) > len(word):
                return 
            
            arr.append(board[row][col]); visited.add((row, col));
            dfs(row + 1, col); dfs(row - 1, col); dfs(row, col + 1); dfs(row, col - 1);
            popped = arr.pop(); visited.remove((row, col))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] not in visited:
                    dfs(row, col)
                    if final == True:
                        return True
        
        return False

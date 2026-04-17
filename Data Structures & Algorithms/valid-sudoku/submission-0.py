class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            r_set = set()
            for elt in row:
                if elt not in r_set and elt != ".":
                    r_set.add(elt)
                elif elt!= "." and elt in r_set:
                    print("Invalid Row", row)
                    return False
            r_set.clear()
        
        for c in range (9):
            c_set = set()
            for r in range(9):
                if board[r][c] not in c_set and board[r][c] != ".":
                    c_set.add(board[r][c])
                elif board[r][c] in c_set and board[r][c] != ".":
                    print("Invalid Column")
                    return False
            c_set.clear()

        square_map = {}
        for row in range(9):
            r_i = row//3
            for col in range (9):
                c_i = col // 3
                if r_i * 3 + c_i not in square_map and board[row][col] != ".":
                    square_map[r_i * 3 + c_i] = set(board[row][col])
                elif r_i * 3 + c_i in square_map:
                    if board[row][col] in square_map.get(r_i * 3 + c_i):
                        print("Invalid Square")
                        print(square_map)
                        return False
        
        return True
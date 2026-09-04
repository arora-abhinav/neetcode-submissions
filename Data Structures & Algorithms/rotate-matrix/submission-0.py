class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #old x,y to new x,y = y,x
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col] = [matrix[row][col], 0]
        
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[col][row][1] = matrix[row][col][0]
        
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col] = matrix[row][col][1]
        
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]
            
        
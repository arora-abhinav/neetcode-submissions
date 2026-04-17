class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = (len(matrix[0]) * len(matrix)) - 1
        while low <= high:
            middle = (low + high) // 2
            row = middle // len(matrix[0])
            col = middle % len(matrix[0])
            if target > matrix[row][col]:
                low = middle + 1
            elif target < matrix[row][col]:
                high = middle - 1
            else:
                return True
        
        return False
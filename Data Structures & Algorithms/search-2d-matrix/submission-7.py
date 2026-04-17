import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_len = len(matrix) * len(matrix[0])
        high = total_len - 1
        low = 0
        while high >= low:
            mid = low + ((high - low)//2)
            row_ind = math.floor(mid/len(matrix[0]))
            col_ind = mid % len(matrix[0])
            if target > matrix[row_ind][col_ind]:
                low = mid + 1
            elif target < matrix[row_ind][col_ind]:
                high = mid - 1
            else:
                return True
        
        return False
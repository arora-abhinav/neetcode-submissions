class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        right_side_prod = [1] * arr_len
        left_side_prod = [1] * arr_len
        for i in range(1, arr_len):
            left_side_prod[i] = nums[i - 1] * left_side_prod[i-1]
        
        for i in range(arr_len - 2, -1, -1):
            right_side_prod[i] = nums[i + 1] * right_side_prod[i + 1]

        res = []
        for i in range(arr_len):
            entry = left_side_prod[i] * right_side_prod[i]
            res.append(entry)
        
        return res
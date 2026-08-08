class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {nums[i]: i for i in range(len(nums))}
        for index, num in enumerate(nums):
            res = target - num
            if res in num_map and num_map[res] != index:
                return [min(index, num_map[res]), max(index, num_map[res])]
        
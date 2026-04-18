class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i
        
        index = 0
        for i in range(len(nums)):
            if target - nums[i] in num_map and i != num_map[target-nums[i]]:
                index = num_map[target-nums[i]]
                return [min(index, i), max(index, i)]
        
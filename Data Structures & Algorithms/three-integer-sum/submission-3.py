class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: 
                continue
            s, e = i + 1, len(nums) - 1
            while s < e: 
                target = -1 * num
                if nums[s] + nums[e] > target: 
                    e -= 1
                elif nums[s] + nums[e] < target: 
                    s += 1
                else: 
                    output.append([num, nums[s], nums[e]])
                    s += 1
                    e -= 1
                    while e > 0 and nums[e] == nums[e + 1]: 
                        e -= 1
                    while s < len(nums) - 1 and nums[s] == nums[s - 1]: 
                        s += 1
        return output
            
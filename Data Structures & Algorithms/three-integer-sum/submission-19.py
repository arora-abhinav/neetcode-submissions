class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for ind, num in enumerate(nums):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            i, j = ind + 1, len(nums) - 1
            target = 0 - num
            while i < j:
                s = nums[i] + nums[j]
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    res.add((num, nums[i], nums[j]))
                    i += 1
                    j -= 1

        
        final = [list(i) for i in res]
        return final
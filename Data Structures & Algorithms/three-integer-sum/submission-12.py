class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for ind in range(len(nums)):
            if nums[ind] > 0:
                break
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue 
            i = ind + 1
            j = len(nums) - 1
            while j > i:
                s = nums[i] + nums[j]
                if s == -nums[ind]:
                    res.append([nums[i], nums[j], nums[ind]])

                    while i + 1 < len(nums) and nums[i] == nums[i+1]:
                        i += 1
                    i += 1

                    while j - 1 >= 0 and nums[j] == nums[j-1]:
                        j -= 1
                    j -= 1
                
                elif s < -nums[ind]:
                    i += 1

                elif s > -nums[ind]:
                    j -= 1
        
        return res
                
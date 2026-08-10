class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[r]:
                return self.binary_search(l, r, nums, target)
            
            elif nums[mid] >= nums[l]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
            
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1

        return -1
    
    def binary_search(self, l, r, nums, target):
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        lo = 0
        while hi >= lo:
            mid = lo + ((hi - lo)//2)
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid
        
        return -1
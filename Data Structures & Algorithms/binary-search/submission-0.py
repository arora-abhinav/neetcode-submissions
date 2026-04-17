class Solution:
    def recur(self, low: int, high: int, nums: List[int], target) -> int:
        if low > high:
            return -1
            
        mid = (low + high)//2
        if nums[mid] > target:
            return self.recur(low, mid -1, nums, target)
        elif nums[mid] < target:
            return self.recur(mid + 1, high, nums, target)
        else:
            return mid
    

    def search(self, nums: List[int], target: int) -> int:

        return self.recur(0, len(nums) -1, nums, target)

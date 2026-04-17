
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        arr = [set() for _ in range(len(nums) + 1)]
        h_set = set()

        for i in nums:
            h_set.add(i)

        for j in nums:
            temp = j
            count = 1
            while temp + 1 in h_set:
                count += 1
                temp += 1
            arr[count].add(temp)

        for k in range(len(arr) - 1, -1, -1):
            if len(arr[k]) != 0:
                return k

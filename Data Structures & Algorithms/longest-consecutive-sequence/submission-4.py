
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        h_set = set()
        arr = [[]]
        for i in nums:
            h_set.add(i)
        
        
        longest = 0
        for k in h_set:
            if k - 1 not in h_set:
                length = 1
                while k + length in h_set:
                    length +=1
                if length > longest:
                    longest = length
            
        return longest


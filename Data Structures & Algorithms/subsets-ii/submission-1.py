class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for num in nums:
            l = len(res)
            for i in range(l):
                arr = res[i].copy()
                arr.append(num)
                if sorted(arr) not in res:
                    res.append(arr)

        return res
                
            
            



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        res2 = set()
        for num in nums:
            l = len(res)
            for i in range(l):
                arr = res[i].copy()
                arr.append(num)
                if tuple(arr) not in res2:
                    res.append(arr)
                    res2.add(tuple(arr))

        return res
                
            
            



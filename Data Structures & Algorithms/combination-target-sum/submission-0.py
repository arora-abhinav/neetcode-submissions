class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def DFS(i, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target or i > len(nums) - 1:
                return 
            
            #Either include it or don't include the current number
            arr.append(nums[i])
            DFS(i, arr, total + nums[i])
            arr.pop()
            DFS(i + 1, arr, total)
        
        DFS(0, [], 0)
        return res
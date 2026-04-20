class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        subset = []
        nums = sorted(nums)
        def dfs(i):
            if i >= len(nums):
                subsets.add(tuple(subset.copy()))
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        subsets = list(subsets)
        return [list(x) for x in subsets]
        

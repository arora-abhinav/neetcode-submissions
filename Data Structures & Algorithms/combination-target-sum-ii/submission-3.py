class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sums = []
        candidates.sort()
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sums.copy())
                return
            if cur_sum > target or i >= len(candidates):
                return

            if cur_sum + candidates[i] >target:
                return
                
            
            sums.append(candidates[i])
            cur_sum += candidates[i]
            backtrack(i + 1 ,cur_sum)
            sums.pop()
            cur_sum -= candidates[i]

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, cur_sum)
        
        backtrack(0, 0)
        return res
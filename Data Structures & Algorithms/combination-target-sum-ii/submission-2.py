class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        sub = []
        candidates = sorted(candidates)
        def dfs(i, cur_sum):
            if cur_sum == target:
                res.add(tuple(sub.copy()))
                return
            
            if i >= len(candidates) or cur_sum > target:
                return 
            sub.append(candidates[i])
            cur_sum += candidates[i]
            dfs(i + 1, cur_sum)
            sub.pop()

            cur_sum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
                
            dfs(i+1, cur_sum)
        
        dfs(0, 0)
        return [list(i) for i in res]
from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        can_counter = Counter(candidates)
        c_set = set(candidates)
        c_set = list(c_set)
        cur_count = defaultdict(int)
        res = []; cur = []; c_sum = 0;
        c_set.sort()
        def dfs(i):
            nonlocal c_sum
            if cur:
                if cur_count[cur[-1]] > can_counter[cur[-1]]:
                    return
            if i > len(c_set) - 1 or c_sum > target:
                return
            if c_sum == target:
                res.append(cur[:])
                return
            cur.append(c_set[i])
            cur_count[c_set[i]] += 1
            c_sum += c_set[i]
            dfs(i)
            popped = cur.pop()
            c_sum -= popped
            cur_count[popped] -= 1
            dfs(i + 1)
            return
        
        dfs(0)
        return res
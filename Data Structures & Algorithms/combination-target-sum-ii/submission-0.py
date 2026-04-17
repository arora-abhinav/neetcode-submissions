class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        h_map = {}
        for i in candidates:
            if i not in h_map:
                h_map[i] = 1
            else:
                h_map[i] += 1
        
        candidates.sort()

        c = []
        dups = set()
        for i in candidates:
            if i not in dups:
                dups.add(i)
                c.append(i)
        res = []

        print(h_map)
        print(c)

        def DFS(i, arr, total, occurences):
            if total > target or i > len(c) - 1:
                return
            if occurences > h_map[c[i]]:
                return 
            if total == target:
                res.append(arr.copy())
                return
            
            arr.append(c[i])
            DFS(i, arr, total + c[i], occurences + 1)
            arr.pop()
            DFS(i + 1, arr, total, 0)
        
        DFS(0, [], 0, 0)
        return res
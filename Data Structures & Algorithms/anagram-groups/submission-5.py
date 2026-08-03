class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            i = tuple(sorted(Counter(s).items()))
            print(i)
            if i not in res:
                res[i] = []
            res[i].append(s)
        
        final_res = []
        for r in res:
            final_res.append(res[r])
        
        return final_res
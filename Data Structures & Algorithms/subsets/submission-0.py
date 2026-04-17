class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for i in nums:
            l = len(out)
            for j in range(l):
                copy = []
                for elt in out[j]:
                    copy.append(elt)
                copy.append(i)
                out.append(copy)
        
        return out
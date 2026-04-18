import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappings = Counter(nums)
        res = []
        for i in mappings:
            res.append((i, mappings[i]))
        heapq.heapify_max(res)
        new = heapq.nlargest(k, res, key=lambda item:item[1])
        print(new)
        res.clear()
        for tup in new:
            num, freq = tup
            res.append(num)
        
        return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        s = 0
        while l <= r:
            mid = (l + r)//2
            s = sum(math.ceil(float(p)/mid) for p in piles)
            print(s)
            if s > h:
                l = mid + 1
            elif s <= h:
                res = mid
                r = mid - 1
        
        return res
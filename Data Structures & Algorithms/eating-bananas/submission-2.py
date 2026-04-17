import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 1
        high = piles[-1]
        
        while low <= high:
            mid = (low + high)//2
            s = 0
            for i in range(len(piles)):
                s += math.ceil(piles[i] / mid)
            
            if h >= s:
                high = mid - 1
            else:
                low = mid + 1

                
        return low

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low < high:
            mid = (low + high)//2

            rate = sum(math.ceil(pile/mid) for pile in piles)
            
            print(rate)
            if rate <= h:
                high = mid 
            else:
                low = mid + 1

        return low
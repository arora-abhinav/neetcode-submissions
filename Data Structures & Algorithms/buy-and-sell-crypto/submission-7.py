class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        diff = 0
        while right < len(prices) :
            diff = max(diff, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1

        return diff
        
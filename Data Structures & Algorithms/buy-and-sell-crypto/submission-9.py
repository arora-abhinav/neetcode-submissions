class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            profit = max(profit, prices[j] - prices[i])
            if prices[i] >= prices[j]:
                i = j
            j+= 1

        return profit
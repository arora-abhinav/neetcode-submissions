class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Suffix arrays:
        suffix_arr = [0] * len(prices)
        suffix_arr[len(prices) - 1] = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            suffix_arr[i] = max(prices[i], suffix_arr[i+1])
        
        print(suffix_arr)
        max_profit = 0
        for i in range(len(suffix_arr)):
            max_profit = max(max_profit, suffix_arr[i] - prices[i])
        return max_profit
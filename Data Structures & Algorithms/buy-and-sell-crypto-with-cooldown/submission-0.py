from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        def dfs(canBuy, i):
            if i >= len(prices): 
                return 0
            if (canBuy, i) in dp:
                return dp[(canBuy, i)]
            
            if canBuy == True:
                dp[(canBuy, i)] = max(-prices[i] + dfs(False, i + 1), dfs(True, i + 1))
            else:
                dp[(canBuy, i)] = max(prices[i] + dfs(True, i + 2), dfs(False, i + 1))
            
            return dp[(canBuy, i)]
        
        return dfs(True, 0)
        
            
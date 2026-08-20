from collections import defaultdict
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [float('inf')] * len(cost)
        
        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != float('inf'):
                return memo[i]
            memo[i] = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
            return memo[i]
        
        dfs(0)
        return min(memo[0], memo[1])
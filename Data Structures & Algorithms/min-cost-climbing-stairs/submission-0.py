class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        
        def dfs(i, c):
            if i == len(cost):
                return c
            if i > len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i + 1, c), dfs(i + 2, c))
            return cache[i]
        
        return min(dfs(0, 0), dfs(1, 0))
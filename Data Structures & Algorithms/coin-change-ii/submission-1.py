class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        dp = {}
        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if i >= len(coins) or remaining < 0:
                return 0
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            total = 0; total += dfs(i, remaining - coins[i]) + dfs(i + 1, remaining);

            dp[(i,remaining)] = total
            return total

        
        return dfs(0, amount)

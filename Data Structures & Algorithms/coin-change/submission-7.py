class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1); dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                remaining = a - c
                if remaining >= 0:
                    dp[a] = min(dp[a], 1 + dp[remaining])


        return dp[amount] if dp[amount] != float('inf') else -1
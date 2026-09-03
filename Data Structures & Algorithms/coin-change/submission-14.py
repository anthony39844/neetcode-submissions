class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                x = i - coin
                dp[i] = min(1 + dp[x], dp[i])
        
        return dp[amount] if dp[amount] != float('inf') else -1
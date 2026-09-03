class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Using amount + 1 as infinity keeps operations purely integer-based
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 2)
        
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[1]
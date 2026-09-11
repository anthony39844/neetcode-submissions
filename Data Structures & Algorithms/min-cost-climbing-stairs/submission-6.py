class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [i for i in cost]
        for i in range(len(cost) - 3, -1, -1):
            dp[i] += min(dp[i+2], dp[i+1])
        
        return min(dp[0], dp[1])
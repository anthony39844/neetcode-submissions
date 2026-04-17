class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        min_p = prices[0]
        for i in prices:
            min_p = min(min_p, i)
            out = max(out, i - min_p)
        return out
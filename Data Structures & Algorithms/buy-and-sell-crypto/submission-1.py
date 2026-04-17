class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        l, r = 0, 1
        while r < len(prices):
            out = max(out, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
            

        return out
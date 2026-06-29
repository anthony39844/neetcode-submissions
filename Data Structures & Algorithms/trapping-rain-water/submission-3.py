class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        out = 0
        while l < r:
            if maxL >= maxR:
                out += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
            else:
                out += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
        return out
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]
        area = 0
        while l < r:
            if heights[l] > maxL:
                maxL = heights[l]
            if heights[r] > maxR:
                maxR = heights[r]
            area = max(area, min(maxL,maxR) * (r - l))
            print(area)
            if maxR > maxL:
                l += 1
            else:
                r -= 1
        return area
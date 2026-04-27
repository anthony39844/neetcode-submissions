class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        out = 0

        heights.append(0)

        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                x = s.pop()

                if not s:
                    w = i
                else:
                    w = i - s[-1] - 1
                
                out = max(out, heights[x] * w)
            
            s.append(i)
    
        return out
                

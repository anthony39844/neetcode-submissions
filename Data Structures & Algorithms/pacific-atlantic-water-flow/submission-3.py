class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        out = []

        def pac(i, j, visited):
            if i <= 0 or j <= 0:
                return True
            
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(heights) and 0 <= b < len(heights[0]) and heights[a][b] <= heights[i][j] and (a, b) not in visited:
                    visited.add((a, b))
                    if pac(a, b, visited):
                        return True
            
            return False
        
        def atl(i, j, visited):
            if i >= len(heights) - 1  or j >= len(heights[0]) - 1:
                return True
            
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(heights) and 0 <= b < len(heights[0]) and heights[a][b] <= heights[i][j] and (a, b) not in visited:
                    visited.add((a, b))
                    if atl(a, b, visited):
                        return True

            return False
                
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pac(i, j, set()) and atl(i, j, set()):
                    out.append([i, j])
        
        return out
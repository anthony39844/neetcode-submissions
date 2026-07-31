class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        out = 0
        area = 0

        def func(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            nonlocal area
            area += 1
            grid[i][j] = 0
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                func(i + x, j + y)
                
            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = 0
                    func(i, j)
                    out = max(out, area)
        
        return out
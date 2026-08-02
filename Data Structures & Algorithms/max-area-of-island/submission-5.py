class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        out = 0

        def dfs(i, j):
            area = 1
            grid[i][j] = 0

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == 1:
                    area += dfs(a, b)
            
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    out = max(out, dfs(i, j))
        
        return out

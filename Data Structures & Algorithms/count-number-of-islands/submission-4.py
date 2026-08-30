class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0

        def dfs(i, j):
            
            grid[i][j] = "0"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == "1":
                    dfs(a, b)
            
            return True
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and dfs(i, j):
                    out += 1
        
        return out
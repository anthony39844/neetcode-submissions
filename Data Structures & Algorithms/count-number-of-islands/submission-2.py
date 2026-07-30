class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0

        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(x, y):
            
            grid[x][y] = "#"
            for i, j in directions:
                a, b = x + i, y + j
                if (a, b) not in visited and 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == "1":
                    bfs(a, b)

            return True

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    if bfs(i, j):
                        out += 1
        
        return out

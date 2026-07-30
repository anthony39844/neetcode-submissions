class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0

        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            if grid[x][y] == "0":
                return False
            
            visited.add((x, y))
            for i, j in directions:
                a, b = x + i, y + j
                if (a, b) not in visited:
                    bfs(a, b)

            return True

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    if bfs(i, j):
                        out += 1
        
        return out

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append([i, j, 0])

        while q:
            x, y, count = q.popleft()
    
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == 2147483647:
                    grid[a][b] = count + 1
                    q.append((a, b, count+1))

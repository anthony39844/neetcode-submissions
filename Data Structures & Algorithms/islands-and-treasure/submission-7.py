class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j))

        count = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = min(count, grid[x][y])
                for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a, b = x + i, y + j
                    if (0 <= a < len(grid) and 0 <= b < len(grid[0])):
                        if grid[a][b] == 2147483647:
                            q.append((a, b))
            count += 1

    


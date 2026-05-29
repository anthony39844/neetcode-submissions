class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        q = deque()

        # gather all the treasure chests
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                   q.append((i, j))

        # since we spread out one layer at a time, the first time a cell is reached, 
        # that is the shortest path 
        while q:
            # for each chest, bfs
            i, j = q.popleft()
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if (0 <= a < m and 0 <= b < n) and grid[a][b] == INF:
                    q.append((a, b))
                    # since chest have initially a value of 0, this can keep track of the distance
                    grid[a][b] = grid[i][j] + 1

        return
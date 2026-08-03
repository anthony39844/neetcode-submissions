class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j))

        count = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                visited.add((i, j))
                grid[i][j] = min(count, grid[i][j])

                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a, b = i + x, j + y
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == 2147483647:
                        q.append((a, b))

            count += 1


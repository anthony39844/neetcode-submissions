class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        out = 0
        while q:
            if fresh == 0:
                return out
            for _ in range(len(q)):
                x, y = q.popleft()

                for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a, b = x + i, y + j
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == 1:
                        fresh -= 1
                        q.append((a, b))
                        grid[a][b] = 2
            out += 1

        return out if fresh == 0 else -1
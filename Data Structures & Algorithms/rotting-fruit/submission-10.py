class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        out = 0
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
                
        if fresh == 0:
            return 0

        while q:
            for i in range(len(q)):
                i, j = q.popleft()

                for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = i + a, j + b
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh -= 1

            out += 1
            if fresh == 0:
                return out

        return out if fresh == 0 else -1
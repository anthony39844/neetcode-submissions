class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        time = 0
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh+=1
                if grid[row][col] == 2:
                    q.append((row,col))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    newr = dr+r
                    newc = dc+c
                    if min(newr,newc) <0 or newr==rows or newc==cols or grid[newr][newc] == 0 or grid[newr][newc]==2:
                        continue
                    grid[newr][newc] = 2
                    q.append((newr,newc))
                    fresh -=1
            time +=1

        if fresh == 0:
            return time
        else:
            return -1        

        

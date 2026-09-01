class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        out = []
        pac = set()
        atl = set()
        m, n = len(heights), len(heights[0])

        def dfs(x, y, ocean):
            ocean.add((x, y))
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if 0 <= a < m and 0 <= b < n and heights[a][b] >= heights[x][y] and (a, b) not in ocean:
                    dfs(a, b, ocean)
            
        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n-1, atl)
        
        for i in range(n):
            dfs(0, i, pac)
            dfs(m-1, i, atl)
        
        return list(atl & pac)

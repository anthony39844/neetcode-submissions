class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        atl = set()
        pac = set()

        def dfs(i, j, visited):
            
            visited.add((i, j))
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(heights) and 0 <= b < len(heights[0]) and heights[a][b] >= heights[i][j] and (a, b) not in visited:
                    dfs(a, b, visited)

        for i in range(len(heights)):
            dfs(i, 0, pac)
            dfs(i, len(heights[0]) - 1, atl)
        
        for i in range(len(heights[0])):
            dfs(0, i, pac)
            dfs(len(heights) - 1, i, atl)
        
        return list(pac & atl)
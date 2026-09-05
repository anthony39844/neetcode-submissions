class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        out = 0
        visited = [0] * n
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node):
            visited[node] = 1
            for neigh in adj[node]:
                if visited[neigh] == 0:
                    dfs(neigh)

        
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                out += 1
        
        return out

            
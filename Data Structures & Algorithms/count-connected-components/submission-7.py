class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        out = 0
        visited = set()
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for i in adj[node]:
                dfs(i)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                out += 1
        
        return out
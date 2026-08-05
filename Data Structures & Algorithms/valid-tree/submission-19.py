class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        visited = set()

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    dfs(neigh)
            return True

        dfs(0)
        return len(visited) == n


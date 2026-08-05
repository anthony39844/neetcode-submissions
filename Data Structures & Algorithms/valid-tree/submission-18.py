class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:
            return False

        adj = defaultdict(list)
        visited = set()

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node, parent):
            if node in visited:
                return False
                
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False

            return True

        if not dfs(0, None): 
            return False

        return len(visited) == n


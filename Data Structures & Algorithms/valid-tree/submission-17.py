class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        visited = set()
        seen = set()

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node, parent):
            if node in visited:
                return False
                
            seen.add(node)
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            visited.remove(node)

            return True

        if not dfs(0, None): 
            return False

        return True if len(seen) == n else False


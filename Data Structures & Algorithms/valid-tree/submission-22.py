class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        completed = set()
        def dfs(node, parent):
            if node in completed:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            visited.remove(node)
            completed.add(node)
            return True
        
        dfs(0, None)
        
        print(completed)
        return len(completed) == n
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        adj = defaultdict(list)

        def dfs(node, target):
            if node == target:
                return True
            
            visited.add(node)
            for n in adj[node]:
                if n not in visited:
                    if dfs(n, target):
                        return True
            visited.remove(node)

        for x, y in edges:
            if x in adj and y in adj and dfs(x, y):
                return [x, y]
            adj[x].append(y)
            adj[y].append(x)
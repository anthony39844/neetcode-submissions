class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in graph[node]:
                if neigh != parent:
                    if not dfs(neigh, node):
                        return False
            visited.remove(node)
            return True

        for i in range(n):
            if not dfs(i, None):
                return False
        
        return True
        
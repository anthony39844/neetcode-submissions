class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set([0])
        q = deque([0])
        while q:
            node = q.popleft()

            for neigh in adj[node]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        
        return len(visited) == n


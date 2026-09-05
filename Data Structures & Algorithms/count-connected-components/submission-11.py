class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        out = 0
        visited = [0] * n
        adj = defaultdict(list)
        q = deque()

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        for i in range(n):
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                while q:
                    node = q.popleft()
                    for neigh in adj[node]:
                        if visited[neigh] == 0:
                            visited[neigh] = 1
                            q.append(neigh)
                out += 1
        
        return out
            
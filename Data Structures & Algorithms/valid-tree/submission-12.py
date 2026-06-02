class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        q = deque([(0, None)])
        visited = {0}

        while q:
            node, parent = q.popleft()

            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False

                visited.add(neigh)
                q.append([neigh, node])

        return len(visited) == n
        
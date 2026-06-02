class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        q = deque([(0, None)])
        visited = set()

        while q:
            node, parent = q.popleft()
            visited.add(node)

            for neigh in graph[node]:
                if node != parent and neigh not in visited:
                    q.append([neigh, node])
        print(len(visited))
        return len(visited) == n
        
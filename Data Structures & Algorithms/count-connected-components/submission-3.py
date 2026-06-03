class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 0:
            return 0

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        q = deque()
        visited = set()
        count = 0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                count += 1
                q.append(node)

            while q:
                node = q.popleft()
                
                for i in graph[node]:
                    if i not in visited:
                        visited.add(i)
                        q.append(i)

        return count


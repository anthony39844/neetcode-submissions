class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 0:
            return 0

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        q = deque([(0)])
        visited = {0}
        count = 0

        while graph:
            
            while q:
                node = q.popleft()
                
                for i in graph[node]:
                    if i not in visited:
                        visited.add(i)
                        q.append(i)
                
                del graph[node]
            if graph:
                q.append(next(iter(graph)))
            count += 1

        return n - len(visited) + count


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            degree[course] += 1
        
        q = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)

        out = []
        while q:
            course = q.popleft()
            out.append(course)

            for c in adj[course]:
                degree[c] -= 1
                if degree[c] == 0:
                    q.append(c)
        
        return out if len(out) == numCourses else []
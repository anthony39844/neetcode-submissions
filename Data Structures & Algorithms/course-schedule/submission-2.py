class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        print(adj)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
          

            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        out = []

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        completed = set()

        def dfs(course):
            if course in completed:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            out.append(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return out

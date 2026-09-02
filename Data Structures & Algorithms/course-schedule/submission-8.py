class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        completed = set()
        visited = set()
        def dfs(node):
            if node in completed:
                return True
            if node in visited:
                return False
            visited.add(node)
            for course in adj[node]:
                if not dfs(course):
                    return False
            visited.remove(node)
            completed.add(node)
            return True
                

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
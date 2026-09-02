class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        completed = set()

        def dfs(node, visited):
            if node in completed:
                return True
            if node in visited:
                return False
            visited.add(node)
            for course in adj[node]:
                if not dfs(course, visited):
                    return False
            completed.add(node)
            return True
                

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True
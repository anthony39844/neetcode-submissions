class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        completed = set()

        def dfs(node):
            if node in visited:
                return False
            if node in completed:
                return True
            
            visited.add(node)
            for course in adj[node]:
                if not dfs(course):
                    return False
            visited.remove(node)
            completed.add(node)
            out.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return out
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 2:
                return True
            if visited[node] == 1:
                return False

            visited[node] = 1
            for course in adj[node]:
                if not dfs(course):
                    return False
            visited[node] = 2
            return True
                

        for i in range(numCourses):
            if visited[i] == 2:
                continue
            
            if not dfs(i):
                return False
        
        return True
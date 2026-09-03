class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        adj = defaultdict(list)
        visited = [0] * numCourses

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        
        def dfs(course):
            if visited[course] == 2:
                return True
            if visited[course] == 1:
                return False
            visited[course] = 1
            for c in adj[course]:
                if not dfs(c):
                    return False
            
            visited[course] = 2
            out.append(course)

            return True
        
        for i in range(numCourses):
            if visited[i] != 2:
                if not dfs(i):
                    return []
        
        return out
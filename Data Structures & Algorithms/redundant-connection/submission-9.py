class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        forest = [i for i in range(len(edges) + 1)]
        def find(node):
            if forest[node] != node:
                forest[node] = find(forest[node])
            return forest[node]

        for x, y in edges:
            a = find(x)
            b = find(y)

            if a == b:
                return [x, y]
            
            forest[a] = b
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # init every nodes parent as itself
        parent = [i for i in range(len(edges) + 1)]

        # find the parent of a node
        def find(node):
            if parent[node] != node:
                # path compression, set the parent of a node to its top parent node
                parent[node] = find(parent[node])
            return parent[node]

        for x, y in edges:
            a = find(x)
            b = find(y)

            # if parents are the same, then it will create a cycle
            if a == b:
                return [x, y]
            
            # arbitrary, set the parent of a to b, could be b to a if you wanted
            parent[a] = b
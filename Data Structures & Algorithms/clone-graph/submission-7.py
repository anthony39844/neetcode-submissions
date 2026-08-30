"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        d = {}
        
        def dfs(cur):
            if cur in d: return d[cur]
            d[cur] = Node(cur.val)
            for neigh in cur.neighbors:
                dfs(neigh)
                d[cur].neighbors.append(d[neigh])
            
        dfs(node)
        return d[node]
            
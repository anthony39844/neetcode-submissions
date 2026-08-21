# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k

        def dfs(node):
            if not node:
                return None

            x = dfs(node.left)
            if x: return x

            self.k -= 1
            if self.k == 0:
                return node.val
            
            x = dfs(node.right)
            if x: return x

            return None
        
        return dfs(root)
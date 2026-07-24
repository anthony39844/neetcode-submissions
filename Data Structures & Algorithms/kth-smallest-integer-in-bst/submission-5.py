# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = k

        def dfs(node):
            if not node:
                return 
            
            nonlocal i
            x = dfs(node.left)
            if x: return x

            i -= 1
            if i == 0:
                return node.val
    
            x = dfs(node.right)
            if x: return x
        
        return dfs(root)
      
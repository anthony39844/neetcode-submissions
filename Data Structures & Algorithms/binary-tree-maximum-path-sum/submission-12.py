# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.out = root.val

        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            self.out = max(self.out, node.val, node.val + l, node.val + r, node.val + l + r) # what is the global max 
            return max(node.val, node.val + l, node.val + r)
        
        dfs(root)
        return self.out

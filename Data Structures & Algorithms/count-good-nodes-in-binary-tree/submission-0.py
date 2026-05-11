# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.out = 0

        def dfs(node, val):
            if not node:
                return 0

            count = 1 if node.val >= val else 0
            val = max(node.val, val)

            return count + dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, root.val)
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        out = 0
        def dfs(node, parent):
            nonlocal out
            if not node:
                return
            if not parent or (parent and node.val >= parent.val):
                out += 1
                dfs(node.left, node)
                dfs(node.right, node)
            else:
                dfs(node.left, parent)
                dfs(node.right, parent)

            
        dfs(root, None)
        return out
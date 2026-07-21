# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x, y = p, q
        if p.val > q.val:
            x, y = q, p

        if root.val >= x.val and root.val <= y.val:
            return root
        elif root.val > x.val and root.val > y.val:
            return self.lowestCommonAncestor(root.left, x, y)
        elif root.val < x.val and root.val < y.val:
            return self.lowestCommonAncestor(root.right, x, y)
        
        
        
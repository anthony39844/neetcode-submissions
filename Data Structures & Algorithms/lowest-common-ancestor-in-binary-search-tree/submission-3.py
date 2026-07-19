# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x, y = p.val, q.val
        if p.val > q.val:
            x, y = y, x

        def dfs(node):
            
            if (node.val > x and node.val < y) or node.val == x or node.val == y:
                return node
            elif node.val < x and node.val < y:
                return dfs(node.right)
            elif node.val > x and node.val > y:
                return dfs(node.left)
        
        print(dfs(root).val)
        return dfs(root)

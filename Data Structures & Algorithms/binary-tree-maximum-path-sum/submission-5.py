# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = root.val
        def dfs(node):
            nonlocal maxVal
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            print(node.val, maxVal, l, r)
            total = max(node.val + l, node.val + r, node.val)
            maxVal = max(maxVal, total, node.val + l + r)

            return total

        dfs(root)
        return maxVal
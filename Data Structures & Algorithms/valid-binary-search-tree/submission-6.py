# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, maxV, minV):
            if not node: return True

            if node.val >= maxV or node.val <= minV:
                return False
            
            return dfs(node.left, node.val, minV) and dfs(node.right, maxV, node.val)
            
        return dfs(root, float('inf'), float('-inf'))
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        x = k

        def dfs(node):
            nonlocal x

            if not node:
                return None

            n = dfs(node.left)
            if n: return n
            x -= 1
            print(node.val, x)
            if x == 0:
                return node.val
            n = dfs(node.right)
            if n: return n
        
        return dfs(root)



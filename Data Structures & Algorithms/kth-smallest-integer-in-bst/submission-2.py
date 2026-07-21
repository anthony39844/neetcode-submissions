# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.out = 0
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return None  
            
            dfs(node.left)
            count += 1
            if count == k:
                self.out = node.val
            dfs(node.right)

        dfs(root)
        return self.out
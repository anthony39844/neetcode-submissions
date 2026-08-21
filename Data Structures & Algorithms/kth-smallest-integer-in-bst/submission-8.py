# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.out = 0
        self.k = k

        def dfs(node):
            if not node:
                return None
            if dfs(node.left):
                return True
            self.k -= 1
            if self.k == 0:
                self.out = node.val
                return True
            
            if dfs(node.right):
                return True
            if self.k == 0:
                self.out = node.val
        
        dfs(root)
        return self.out
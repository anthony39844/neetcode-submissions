# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        curr = root
        
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            
            curr = s.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right
      
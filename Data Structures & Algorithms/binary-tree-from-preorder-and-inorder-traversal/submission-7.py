# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorderIdx = 0
        inorderIdxs = {val: idx for idx, val in enumerate(inorder)}

        def dfs(preorderIdx, l, r):
            if preorderIdx >= len(preorder) or l > r:
                return None
            
            rootVal = preorder[preorderIdx]
            inorderIdx = inorderIdxs[rootVal]
            root = TreeNode(rootVal)
            root.left = dfs(preorderIdx + 1, l, inorderIdx - 1)
            root.right = dfs(preorderIdx + (inorderIdx - l) + 1, inorderIdx + 1, r)

            return root

        return dfs(preorderIdx, 0, len(preorder) - 1)
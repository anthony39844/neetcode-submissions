# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:    

        preorderIdx = 0
        idx = {val:i for i, val in enumerate(inorder)}

        def dfs(l, r):
            nonlocal preorderIdx
            if l > r or preorderIdx > len(preorder) - 1:
                return None

            rootVal = preorder[preorderIdx]
            inorderIdx = idx[rootVal]
            root = TreeNode(rootVal)
            preorderIdx += 1
            root.left = dfs(l, inorderIdx - 1)
            root.right = dfs(inorderIdx + 1, r)

            return root
            

        return dfs(0, len(preorder) - 1)
 
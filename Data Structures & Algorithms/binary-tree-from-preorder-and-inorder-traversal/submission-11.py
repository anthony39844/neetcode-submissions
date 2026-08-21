# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
         
        inorderIdxs = {}
        for idx, v in enumerate(inorder):
            inorderIdxs[v] = idx
            
        preorderIdx = 0

        def dfs(l, r):
            nonlocal preorderIdx
            if l > r or preorderIdx >= len(inorder):
                return None

            nodeVal = preorder[preorderIdx]
            node = TreeNode(nodeVal)
            preorderIdx += 1

            node.left = dfs(l, inorderIdxs[nodeVal] - 1)
            node.right = dfs(inorderIdxs[nodeVal] + 1, r)
            
            return node

        return dfs(0, len(inorder) - 1)
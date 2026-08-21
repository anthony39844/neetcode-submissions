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

        def dfs(idx, l, r):
            if l > r or idx >= len(inorder):
                return None

            nodeVal = preorder[idx]
            node = TreeNode(nodeVal)

            node.left = dfs(idx + 1, l, inorderIdxs[nodeVal] - 1)
            node.right = dfs(idx + inorderIdxs[nodeVal] + 1 - l, inorderIdxs[nodeVal] + 1, r)
            
            return node

        return dfs(0, 0, len(inorder) - 1)
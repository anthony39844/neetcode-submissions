# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        need to map the value of each ele in preorder to its index in the inorder arr
        so the dict would look like d[val] = ind
        first element in preorder is the root of the tree
        then the inorder arr can be split into left and right sides
        the second element in the preorder is the 
        '''
    

        inorderIdx = defaultdict()
        preorderToInorder = defaultdict()
        for i, val in enumerate(inorder):
            inorderIdx[val] = i
        for i in preorder:
            preorderToInorder[i] = inorderIdx[i]
        
        root = preorder[0]
        rootIdx = preorderToInorder[root]

        def dfs(node, preorderIdx, l, r):
            if r < l or preorderIdx > len(preorder) - 1:
                return None
            
            rootVal = preorder[preorderIdx]
            inorderIdx = preorderToInorder[rootVal]
            root = TreeNode(inorder[inorderIdx])
            root.left = dfs(root, preorderIdx + 1, l, inorderIdx - 1)
            root.right = dfs(root, preorderIdx + (inorderIdx - l) + 1, inorderIdx + 1, r)

            return root

        out = TreeNode(root)
        out.left = dfs(out, 1, 0, rootIdx - 1)
        out.right = dfs(out, rootIdx + 1, rootIdx + 1, len(preorder) - 1)
        
        return out
 
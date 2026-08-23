# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        out = []
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                out.append("#")
            else:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            
        return ",".join(out)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        arr = data.split(",")
        
        root = TreeNode(arr[0])
        q = deque([root])
        i = 0

        while q:
            node = q.popleft()
            i += 1
            if arr[i] != "#":
                node.left = TreeNode(arr[i])
                q.append(node.left)
            
            i += 1
            if arr[i] != "#":
                node.right = TreeNode(arr[i])
                q.append(node.right)

        return root
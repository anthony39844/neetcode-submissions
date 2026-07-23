# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""

        self.out = []
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == None:
                    self.out.append("None")
                    continue
                self.out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        

        return ",".join(self.out)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None

        arr = data.split(",")
        print(arr)

        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()
            
            if node:
                if arr[i] != "None":
                    node.left = TreeNode(int(arr[i]))
                    q.append(node.left)
                
                i += 1
                if arr[i] != "None":
                    node.right = TreeNode(int(arr[i]))
                    q.append(node.right)
                i += 1
        
        return root




        
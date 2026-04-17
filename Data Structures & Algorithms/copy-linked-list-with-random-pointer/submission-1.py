"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val) if cur.val else None
            cur = cur.next

        for i in d:
            d[i].random = d[i.random] if i.random else None
            d[i].next = d[i.next] if i.next else None
        
        
        return d[head]




        
        

            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        make stack of nodes and get count
        find the split or halfway point
        loop for half - 1, since we start with the 1st node already
        add node from top of stack, set next to none, add node from bottom of stack, set next to none
        if len is even, there is one last node from the top of the stack we need to add
        '''
        
        cur = head
        s = []
        x = 0
        
        while cur:
            s.append(cur)
            cur = cur.next
            x += 1

        half = math.ceil(x / 2)

        for i in range(half - 1):
            head.next = s.pop()
            head = head.next
            head.next = None

            head.next = s[i + 1]
            head = head.next
            head.next = None

        if x % 2 == 0:
            head.next = s.pop()
            head = head.next
            head.next = None


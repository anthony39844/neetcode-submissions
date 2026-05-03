# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        2 pointers, one moving 1 node at a time, the other moving 2 nodes at a time
        if there is a cycle they will eventually end up at the same node
        '''

        fast = head
        slow = head

        if slow == None or fast == None:
            return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
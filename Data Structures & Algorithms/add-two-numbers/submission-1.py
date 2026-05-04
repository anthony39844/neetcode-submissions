# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val
            x = total % 10
            cur.next = ListNode(x + carry)
            carry = total // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            x = total % 10
            cur.next = ListNode(x)
            carry = total // 10
            cur = cur.next
            l1 = l1.next

        while l2:
            total = l2.val + carry
            x = total % 10
            cur.next = ListNode(x)
            carry = total // 10
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next
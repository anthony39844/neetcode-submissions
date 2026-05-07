# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for i, x in enumerate(lists):
            while x:
                heapq.heappush(heap, (x.val, count, x))
                x = x.next
                count += 1
        
        dummy = ListNode()
        cur = dummy

        while heap:
            x, _, node = heapq.heappop(heap)
            node.next = None
            cur.next = node
            cur = cur.next

        return dummy.next

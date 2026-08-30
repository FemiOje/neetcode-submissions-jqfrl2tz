# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        tail = dummy

        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index, node))
        
        while heap:
            curr, i, n = heapq.heappop(heap)
            tail.next = n
            tail = tail.next

            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))
        
        return dummy.next
        
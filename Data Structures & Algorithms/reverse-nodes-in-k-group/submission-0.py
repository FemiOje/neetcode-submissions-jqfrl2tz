# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        to_array  = []
        while head:
            to_array.append(head.val)
            head = head.next
        
        arranged = []
        s = 0
        while s < len(to_array):
            chunk = to_array[s:s+k]
            if len(chunk) == k:
                chunk.reverse()
            arranged.extend(chunk)
            s += k

        dummy = ListNode()
        curr = dummy
        for i in arranged:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
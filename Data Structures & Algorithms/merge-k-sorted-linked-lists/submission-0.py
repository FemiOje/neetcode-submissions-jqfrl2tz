# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for i in range(len(lists)):
            while lists[i]:
                nodes.append(lists[i].val)
                lists[i] = lists[i].next
        nodes.sort()

        dummy = ListNode()
        curr = dummy
        start = 0

        while start < len(nodes):
            curr.next = ListNode(nodes[start])
            curr = curr.next
            start += 1
        return dummy.next
        
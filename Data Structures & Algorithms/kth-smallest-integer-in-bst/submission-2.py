# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        
        lol = []
        q = deque([ root ])
        l = 0
        while q:
            curr = q.popleft()
            lol.append(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        lol.sort()

        return lol[k - 1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        queue = collections.deque([ root ])
        while queue:
            curr = queue.popleft()
            left = curr.left if not None else None
            right = curr.right if not None else None
            curr.left, curr.right = right, left

            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return root
        
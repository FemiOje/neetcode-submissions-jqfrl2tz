# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        queue = deque([(root, -float("inf"))])

        while queue:
            curr, currMax = queue.popleft()
            if curr.val >= currMax: res += 1

            if curr.left: queue.append((curr.left, max(currMax, curr.val)))
            if curr.right: queue.append((curr.right, max(currMax, curr.val)))
        return res
        
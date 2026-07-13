# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        queue = deque([(root, -float("inf"), float("inf"))])

        while queue:
            curr, lBound, rBound = queue.popleft()

            if not lBound < curr.val < rBound:
                return False

            if curr.left:
                queue.append((curr.left, lBound ,curr.val))
            if curr.right:
                queue.append((curr.right, curr.val, rBound))
        
        return True
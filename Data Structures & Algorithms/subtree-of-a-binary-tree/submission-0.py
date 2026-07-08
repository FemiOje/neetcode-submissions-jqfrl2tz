# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True

        def isSameTree(p, q) -> bool:
            if not p and not q: return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        que = deque([ root ])
        while que:
            curr = que.popleft()
            if curr.left: que.append(curr.left)
            if curr.right: que.append(curr.right)
            if isSameTree(curr, subRoot): return True
        return False
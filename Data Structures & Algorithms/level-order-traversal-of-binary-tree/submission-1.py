# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        que = collections.deque([ root ])

        while que:
            levLen = len(que)
            level = []

            for i in range(levLen):
                curr = que.popleft()
                level.append(curr.val)
                if curr.left: que.append(curr.left)
                if curr.right: que.append(curr.right)
            res.append(level)
     
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = collections.deque([ root ])
        
        while queue:
            levelLen = len(queue)
            levelNodes = []

            for node in range(levelLen):
                curr = queue.popleft()
                levelNodes.append(curr.val)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            result.append(levelNodes)
        return result
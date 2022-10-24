from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = deque([])
        stack.appendleft(root.left)
        stack.append(root.right)

        while stack:
            p, q = stack.popleft(), stack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            stack.appendleft(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.appendleft(q.left)
        return True
        

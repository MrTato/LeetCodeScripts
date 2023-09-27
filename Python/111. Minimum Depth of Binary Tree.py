# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = deque()
        q.append((root,1))
        
        while q:
            length = len(q)
            for _ in range(length):
                node, depth = q.popleft()
                left = node.left
                right = node.right
                if not left and not right:
                    return depth
                else:
                    if left: q.append((left, depth + 1))
                    if right: q.append((right, depth + 1))

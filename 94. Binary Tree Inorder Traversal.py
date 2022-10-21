# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:       
        if root is None:
            return []
        output = []
        stack = [(False, root)]
        while stack:
            visited, node = stack.pop()
            if visited:
                output.append(node.val)
                if node.right: stack.append((False,node.right))
            else:
                stack.append((True, node))
                if node.left: stack.append((False, node.left))
        return output

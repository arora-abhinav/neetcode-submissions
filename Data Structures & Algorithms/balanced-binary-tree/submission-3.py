# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        difference = 0
        def inner(current) -> int:
            nonlocal difference

            if not current:
                return 0
            left = inner(current.left)
            right = inner(current.right)
            difference = max(difference, max(left, right) - min(left, right))
            return 1 + max(left, right)
        
        inner(root)
        return difference <= 1
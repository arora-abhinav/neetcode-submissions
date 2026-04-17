# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    def helper(self, current, left, right):
        if not current:
            return True
        if not(current.val > left and current.val < right):
            return False 
        
        return self.helper(current.left, left, current.val) and self.helper(current.right, current.val, right)
    
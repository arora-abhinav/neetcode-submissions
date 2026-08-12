# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            nonlocal res
            nonlocal diff
            diff = max(left, right) - min(left, right)
            if diff > 1:
                return -1
            
            return 1 + max(left, right)
        
        res = dfs(root)
        return False if res == -1 else True
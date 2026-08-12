# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0
        res = True
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            nonlocal diff
            diff = max(left, right) - min(left, right)
            if diff > 1:
                res = res & False
            else:
                res = res & True
            
            return 1 + max(left, right)
        
        dfs(root)
        return res
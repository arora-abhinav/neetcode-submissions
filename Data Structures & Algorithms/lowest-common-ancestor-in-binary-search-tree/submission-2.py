# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        def dfs(root):
            nonlocal res
            if not root or not p or not q:
                return 
            if root.val > max(p.val, q.val):
                dfs(root.left)
            elif root.val < min(p.val, q.val):
                dfs(root.right)
            else:
                res = root
                return
        dfs(root)
        return res
            
            
            

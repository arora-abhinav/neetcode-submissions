# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left_max, right_max):
            if not root:
                return True
            
            if not (left_max < root.val < right_max):
                return False
            
            return True & dfs(root.left, left_max, root.val) & dfs(root.right, root.val, right_max)
        
        return dfs(root, -float('inf'), float('inf'))
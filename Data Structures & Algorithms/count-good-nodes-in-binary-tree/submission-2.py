# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = 1
        def dfs(root, max_num):
            if not root: 
                return 0
            
            s= 0
            if root.val >= max_num:
                max_num = root.val
                s = 1

            return s + dfs(root.left, max_num) + dfs(root.right, max_num)
        
        num += dfs(root.left, root.val) + dfs(root.right, root.val)
        return num


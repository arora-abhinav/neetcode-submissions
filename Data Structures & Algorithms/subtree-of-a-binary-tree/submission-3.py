# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        def checkIsSame(root, subRoot):
            if (not root and subRoot) or (not subRoot and root):
                return False
            
            if not root and not subRoot:
                return True

            if root.val != subRoot.val:
                return False
            left = checkIsSame(root.left, subRoot.left)
            right = checkIsSame(root.right, subRoot.right)

            return True and left and right

        def dfs(root):
            if not root:
                return False
            
            if root.val == subRoot.val:
                res = checkIsSame(root, subRoot)
                if res == True:
                    return res
            
            return False or dfs(root.left) or dfs(root.right)

        return dfs(root)
        
        

            
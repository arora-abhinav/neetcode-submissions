# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def find(node, maxSoFar):
            nonlocal res
            
            if not node:
                return 
            
            if node.val >= maxSoFar:
                res += 1
                maxSoFar = node.val

            find(node.left, maxSoFar)
            find(node.right, maxSoFar)
        
        find(root, float('-inf'))
        return res

        
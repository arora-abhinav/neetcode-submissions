# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = TreeNode()
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        global res
        if self.find(root, p) and self.find(root, q):
            res = root
            self.lowestCommonAncestor(root.left, p, q)
            self.lowestCommonAncestor(root.right, p, q)
        
        return res

    def find(self, current, node) -> bool:
        if not current:
            return False
        if current.val == node.val:
            return True

        return self.find(current.left, node) or self.find(current.right, node)
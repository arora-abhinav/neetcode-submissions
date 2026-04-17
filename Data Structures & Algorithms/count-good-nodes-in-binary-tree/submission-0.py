# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.goodNodesH(root, root.val)
    def goodNodesH(self, current: TreeNode, prev) -> int:
        count = 0
        if current and current.val >= prev:
            count = 1
            prev = current.val
        
        elif not current:
            return count

        return count + self.goodNodesH(current.left, prev) + self.goodNodesH(current.right, prev)
        
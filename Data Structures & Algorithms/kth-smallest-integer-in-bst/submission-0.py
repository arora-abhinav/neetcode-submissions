# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []

        res = -1
        if not root:
            return res

        def inorder(current):
            if current.left:
                inorder(current.left)
            out.append(current.val)
            if current.right:
                inorder(current.right)


        inorder(root)
        print(out)
        return out[k-1]

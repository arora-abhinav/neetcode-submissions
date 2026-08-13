# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m= {val: ind for (ind, val) in enumerate(inorder)}
        pre_idx = 0
        def build(left, right):
            if left > right:
                return None
            nonlocal pre_idx
            val = preorder[pre_idx]
            pre_idx += 1
            mid = m[val]
            root = TreeNode(val)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        
        return build(0, len(inorder)-1)
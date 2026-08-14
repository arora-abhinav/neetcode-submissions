# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {val: ind for (ind, val) in enumerate(inorder)}
        preidx = 0
        def dfs(l, r):
            nonlocal preidx
            if l > r:
                return None
            val = preorder[preidx]
            root = TreeNode(val)
            preidx += 1; mid = m[val];
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
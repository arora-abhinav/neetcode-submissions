from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        if not root:
            return root
        while len(queue) != 0:
            elt = queue.popleft()
            elt.left, elt.right = elt.right, elt.left
            if elt.left:
                queue.append(elt.left)
            if elt.right:
                queue.append(elt.right)
        
        return root
            
        
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return []
        q.append(root)
        while q:
            l = len(q)
            level = []
            for i in range(l):
                elt = q.popleft()
                level.append(elt.val)
                if elt.left:
                    q.append(elt.left)
                if elt.right:
                    q.append(elt.right)
            if level:
                res.append(level)
        
        return res

        
                

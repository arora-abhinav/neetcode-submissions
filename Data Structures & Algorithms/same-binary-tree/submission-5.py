from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        if not p and not q:
            return True
        elif p and not q or q and not p:
            return False
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            e1 = q1.popleft()
            e2 = q2.popleft()
            if e1.val != e2.val:
                return False
            
            if e1.left and not e2.left or e2.left and not e1.left:
                return False

            elif e1.left and e2.left:
                q1.append(e1.left)
                q2.append(e2.left)

            if e1.right and not e2.right or e2.right and not e1.right:
                return False

            elif e1.right and e2.right:
                q1.append(e1.right)
                q2.append(e2.right)
        
        return True
            
        
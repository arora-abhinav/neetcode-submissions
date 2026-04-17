from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        out = []
        q = deque()
        if not root:
            return []
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                elt = q.popleft()
                level.append(elt.val)
                if elt.left:
                    q.append(elt.left)
                if elt.right:
                    q.append(elt.right)
            
            res.append(level)
        
        for arr in res:
            out.append(arr[-1])
        
        return out

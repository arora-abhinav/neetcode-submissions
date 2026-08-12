# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            qLen = len(q)
            arr = []
            for i in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                arr.append(node.val)
            
            if arr:
                res.append(arr)
        final = []
        for arr in res:
            final.append(arr[-1])
        
        return final
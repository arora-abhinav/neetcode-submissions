from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []
        def dfs(root, arr):
            if not root:
                arr.append(None)
                return 
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)

        
        dfs(p, p_arr)
        dfs(q, q_arr)
        
        print(p_arr, q_arr)
        if len(p_arr) != len(q_arr):
            return False
        for i in range(len(p_arr)):
            if p_arr[i] != q_arr[i]:
                return False
        
        return True
            
        
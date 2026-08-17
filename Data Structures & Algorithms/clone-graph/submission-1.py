"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        if not node:
            return None
        def dfs(node, root):
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = root
            for n in node.neighbors:
                root.neighbors.append(dfs(n,  Node(n.val)))
            
            return root
        
        return dfs(node, Node(1))
        
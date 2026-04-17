"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        node_map = {}
        def dfs(cur):
            if cur in node_map:
                return node_map[cur]
            
            new = Node(cur.val)
            node_map[cur] = new
            for n in cur.neighbors:
                new.neighbors.append(dfs(n))
            
            return new
        
        if node:
            return dfs(node)
        return None
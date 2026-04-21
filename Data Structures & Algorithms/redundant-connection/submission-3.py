class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            
            if size[root1] > size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        
        return []
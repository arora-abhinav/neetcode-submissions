class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [i for i in range(len(points))]
        size = [1] * len(points)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a, b):
            root1, root2 = find(a), find(b)
            if root1 == root2:
                return False
            if size[root1] >= size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            return True

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        edges.sort()
        
        total = 0
        edges_used = 0
        for dist, i, j in edges:
            if union(i, j):
                total += dist
                edges_used += 1
                if edges_used == len(points) - 1:
                    return total
        
        return total
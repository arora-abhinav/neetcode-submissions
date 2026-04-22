from collections import deque, defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(deque)
        for source, dest in sorted(tickets):
            graph[source].append(dest)
           
        res = []
        def dfs(node):
            while graph[node]:
                neighbour = graph[node].popleft()
                dfs(neighbour)
            
            res.append(node)

        dfs("JFK")
        return res[::-1]
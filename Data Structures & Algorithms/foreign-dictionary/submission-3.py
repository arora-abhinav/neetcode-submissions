from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set); indegree = defaultdict(int)
        letter_set = set();
        for word in words:
            for letter in word:
                letter_set.add(letter)
                
        for i in range(1, len(words)):
            prev = words[i - 1]; cur = words[i]
            if prev.startswith(cur) and len(prev) > len(cur):
                return ""
            for j in range(min(len(prev), len(cur))):
                if prev[j] == cur[j]:
                    continue
                else:
                    if cur[j] not in graph[prev[j]]:
                        graph[prev[j]].add(cur[j])
                        indegree[cur[j]] += 1
                    break
        
        for letter in letter_set:
            if letter not in indegree:
                indegree[letter] = 0
        
        q = deque();
        for letter in indegree:
            if indegree[letter] == 0:
                q.append(letter)
        
        if len(q) == 0:
            return ""

        print(graph)
        print(indegree)
        
        processed = ""; visited = set()
        while q:
            qLen = len(q)
            for _ in range(qLen):
                popped = q.popleft()
                print(popped)
                processed += popped
                visited.add(popped)
                for n in graph[popped]:
                    if n in visited:
                        continue
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        q.append(n)
        
        return processed if len(processed) == len(indegree) else ""

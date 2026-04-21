from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0 
        
        print(ord("a"))
        print(ord("z"))
        word_set.add(beginWord)
        graph = {word:[] for word in word_set}
        for word in list(word_set):
            for letter in range(len(word)):
                for num in range(97, 123):
                    new = word[:letter] + chr(num) + word[letter + 1:]
                    if new in word_set and new != word:
                        graph[word].append(new)
        
        print(graph)
        processed = 0

        def bfs():
            nonlocal processed
            visited = set()
            q = deque()
            q.append(beginWord)
            visited.add(beginWord)
            while q:
                qLen = len(q)
                for _ in range(qLen):
                    word = q.popleft()
                    if word == endWord:
                        return processed
                    for neighbour in graph[word]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
                processed += 1

            return 0
        res = bfs()
        return res + 1 if res != 0 else 0
                

 

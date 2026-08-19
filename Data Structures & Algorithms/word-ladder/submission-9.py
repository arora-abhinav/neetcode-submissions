from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_set = set(wordList)
        graph = {word: set() for word in wordList}
        graph[beginWord] = set()
        for word in graph:
            for i in range(len(word)):
                for j in range(26):
                    character = chr(ord('a') + j)
                    word_copy = word[:i] + character + word[i+1:]
                    if word_copy in word_set and word_copy != word:
                        graph[word].add(word_copy)

        q = deque()
        q.append(beginWord); processed = 0; visited = set()
        while q:
            qLen = len(q)
            processed += 1
            for _ in range(qLen):
                popped = q.popleft()
                print(popped)
                if popped == endWord:
                    return processed
                if endWord in graph[popped]:
                    q.append(endWord)
                else: 
                    for n in graph[popped]:
                        if n in visited:
                            continue
                        visited.add(n)
                        q.append(n)
        
        return 0

        
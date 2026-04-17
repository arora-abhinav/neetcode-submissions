from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if beginWord == endWord or endWord not in wordList:
            return 0
        visited = set()
        q = deque()  
        q.append(beginWord)
        res = 0
        while q:
            res += 1
            print(q)
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for m in range(len(word)):
                    for k in range(97, 123):
                        new = word[:m] + chr(k) + word[m+1:]
                        if new in words and new not in visited and new!= word:
                            visited.add(new)
                            q.append(new)
        
        return 0
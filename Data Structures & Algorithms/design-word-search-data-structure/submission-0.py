class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode(None)

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TreeNode(letter)
            cur = cur.children[letter]
        cur.end = True
        
    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.end
            if word[i] == ".":
                for character in root.children:
                    if dfs(root.children[character], i + 1):
                        return True
                return False
            if word[i] not in root.children:
                return False
            return dfs(root.children[word[i]], i + 1)
        return dfs(self.root, 0)
        
            



            
        

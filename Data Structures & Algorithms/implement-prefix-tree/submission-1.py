class TreeNode:
    def __init__(self):
        self.children = {}
        self.word_end = ""

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TreeNode()
            cur = cur.children[letter]
        
        cur.word_end = word

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]

        if cur.word_end != word:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            print("Yes")
            cur = cur.children[letter]
        
        return True 
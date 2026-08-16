class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.next = {}

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        self.inserted = set()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.next:
                cur.next[letter] = TreeNode(letter)
            cur = cur.next[letter]
        
        self.inserted.add(word)

    def search(self, word: str) -> bool:
        return True if word in self.inserted else False
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.next:
                return False
            cur = cur.next[letter]
        return True
        
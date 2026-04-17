class PrefixTree:

    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if word == w:
                return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        for w in self.words:
            if w[0: len(prefix)] == prefix:
                return True
        
        return False
        
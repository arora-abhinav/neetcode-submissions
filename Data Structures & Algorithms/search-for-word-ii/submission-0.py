class TreeNode():
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode(None); 
        word_set = set(words)
        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TreeNode(letter)
                cur = cur.children[letter]
            cur.isEnd = True
        
        visited = set(); word = []; found = []
        def dfs(row, col, cur):
            nonlocal word; nonlocal found
            if cur.isEnd == True:
                string = ""
                for w in word:
                    string += w
                if string in word_set:
                    found.append(string)
                    word_set.remove(string)
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or (row, col) in visited or board[row][col] not in cur.children:
                return
            
            visited.add((row, col)); letter = board[row][col];cur = cur.children[letter]; word.append(letter)
            dfs(row + 1, col, cur); dfs(row - 1, col, cur); dfs(row, col + 1, cur); dfs(row, col - 1, cur)
            visited.remove((row, col)); word.pop()

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root)
            
        return found
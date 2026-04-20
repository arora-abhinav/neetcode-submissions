class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        string = []
        def backtrack(i, open_amt, close_amt):
            if i > 2 * n or open_amt > n or close_amt > n or close_amt > open_amt:
                return
            
            if len(string) == 2 * n:
                new = ""
                for char in string:
                    new += char
                res.append(new)
                return
            
            string.append("(")
            backtrack(i + 1, open_amt + 1, close_amt)
            string.pop()
            string.append(")")
            backtrack(i + 1, open_amt, close_amt + 1)
            string.pop()
        
        backtrack(0, 0, 0)
        return res
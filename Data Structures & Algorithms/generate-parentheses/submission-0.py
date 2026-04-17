class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(string, op, cl):
            if cl > op or cl > n or op > n:
                return
            if len(string) == n * 2:
                out = string
                res.append(out)
                return
            string += "("
            backtrack(string, op + 1, cl)
            string = string[:-1]
            string += ")"
            backtrack(string, op, cl + 1)
        
        backtrack("", 0, 0)
        return res
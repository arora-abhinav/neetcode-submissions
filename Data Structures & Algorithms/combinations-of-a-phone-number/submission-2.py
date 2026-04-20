class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        string = []
        res = []
        m = {'2':("A", "B", "C"), '3': ("D", "E", "F"), "4":("G", "H", "I"),
        "5": ("J", "K", "L"), "6":("M", "N", "O"), "7":("P", "Q", "R", "S"), 
        "8": ("T", "U", "V"), "9": ("W", "X", "Y", "Z")}

        def backtrack(i):
            if len(string) == len(digits):
                res.append("".join(string))
                return
            
            for char in m[digits[i]]:
                string.append(char.lower())
                backtrack(i + 1)
                string.pop()
        
        backtrack(0)
        return res
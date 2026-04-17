class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer, sol = [], []
        num_map = {2: ('a', 'b', 'c'),
        3: ('d', 'e', 'f'), 4: ('g', 'h', 'i'), 5: ('j', 'k', 'l'), 
        6: ('m', 'n', 'o'), 7: ('p', 'q', 'r', 's'), 8: ('t', 'u', 'v'),
        9: ('w', 'x', 'y', 'z')}

        def dfs(ind):
            if ind == len(digits) and len(sol) == len(digits) and sol:
                print(sol)
                answer.append("".join(sol))
                return
            
            for j in range(ind, len(digits)):
                for letter in num_map.get(int(digits[j])):
                    sol.append(letter)
                    dfs(j + 1)
                    sol.pop()
        
        dfs(0)
        return answer
            
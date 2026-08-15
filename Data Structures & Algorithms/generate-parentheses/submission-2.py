class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []; open_counter = n; close_counter = n;
        cur = []
        def dfs():
            nonlocal open_counter; nonlocal close_counter;
            if open_counter < 0 or close_counter < 0 or close_counter < open_counter:
                return
            if open_counter == close_counter == 0:
                res.append(cur[:])
                return
            cur.append('('); open_counter -= 1; dfs();
            cur.pop(); open_counter += 1;
            cur.append(')'); close_counter -= 1; dfs();
            cur.pop(); close_counter += 1; 
        
        dfs();
        final = ["".join(i) for i in res]
        return final
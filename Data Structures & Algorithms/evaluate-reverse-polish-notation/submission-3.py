class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '/', '*'])
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                p1 = stack.pop(); p2 = stack.pop();
                res = None;
                if t == '+':
                    res = p2 + p1
                elif t == '*':
                    res = p2 * p1
                elif t == '/':
                    res = int(p2/p1)
                elif t == '-':
                    res = p2 - p1
                
                stack.append(res)
        
        return stack[0]
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set()
        operations.add('+')
        operations.add('-')
        operations.add('*')
        operations.add('/')
        stack = []
        res = 0
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                if token == '+':
                    res = stack[-1] + stack[-2]
                elif token == '*':
                    res = stack[-1] * stack[-2]
                elif token == '/':
                    res = int(stack[-2] / stack[-1])
                elif token == '-':
                    res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            print(stack)
        
        return stack[0]
                
        
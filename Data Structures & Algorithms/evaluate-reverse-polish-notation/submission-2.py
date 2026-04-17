import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {'/': operator.truediv,
        '*': operator.mul, '+': operator.add, '-': operator.sub}
        num_stack = []
        for i in tokens:
            if i not in operator_map:
                num_stack.append(i)
            else:
                s = num_stack.pop()
                f = num_stack.pop()
                res = operator_map[i](int(f), int (s))
                
                num_stack.append(res)
        
        return int(num_stack[0])
        
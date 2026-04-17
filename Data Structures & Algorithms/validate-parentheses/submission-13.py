class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ob_map = {'(':')', '{':'}', '[':']'}
        c_brackets = set()
        c_brackets.add(')')
        c_brackets.add(']')
        c_brackets.add('}')
        if len(s) % 2 != 0:
            return False

        for bracket in s:
            if bracket in ob_map:
                stack.append(bracket)
            if bracket in c_brackets:
                if len(stack) != 0 and ob_map[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_map = {'(' : ')', '[' : ']', '{' : '}'}
        closing_map = {')' : '(', ']' : '[', '}' : '{'}
        for i in range(len(s)):
            print(len(stack))
            if s[i] in opening_map:
                stack.append(s[i])
            else:
                if len(stack) != 0 and stack[-1] == closing_map.get(s[i]):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

            
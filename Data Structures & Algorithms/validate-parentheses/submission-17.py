class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["[", "{", "("]
        closing = ["]", "}", ")"]
        stack = []
        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                ind = closing.index(bracket)
                if stack[-1] == opening[ind]:
                    stack.pop()
                else:
                    stack.append(bracket)
        
        return len(stack) == 0
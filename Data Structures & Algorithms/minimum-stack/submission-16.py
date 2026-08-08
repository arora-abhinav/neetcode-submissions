class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.current_min = min(self.current_min, val)
        self.stack.append((val, self.current_min))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.current_min = self.stack[-1][1]
        else:
            self.current_min = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        

class MinStack:

    def __init__(self):
        self.stack_arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.stack_arr.append(val)
        if not self.min_arr or (self.min_arr and self.min_arr[-1] > val): 
            self.min_arr.append(val)
        else: 
            self.min_arr.append(self.min_arr[-1])

    def pop(self) -> None:
        self.stack_arr.pop()
        self.min_arr.pop()

    def top(self) -> int:
        return self.stack_arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
        

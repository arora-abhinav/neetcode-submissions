class MinStack:

    def __init__(self):
        self.stack_arr = []
        self.min_arr = []
        self.min_num = float('inf')

    def push(self, val: int) -> None:
        self.stack_arr.append(val)
        if self.min_num >= val:
            self.min_num = val
            self.min_arr.append(val)

    def pop(self) -> None:
        elt = self.stack_arr.pop()
        if elt == self.min_num :
            self.min_arr.pop()
            if self.min_arr:
                self.min_num = self.min_arr[-1]
            else: 
                self.min_num = float('inf')

    def top(self) -> int:
        return self.stack_arr[-1]

    def getMin(self) -> int:
        return self.min_num
        

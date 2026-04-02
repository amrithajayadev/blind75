class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_so_far = list()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_so_far:
            self.min_so_far.append(min(val,self.min_so_far[-1]))
        else:
            self.min_so_far.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_so_far.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_so_far[-1]
        

        


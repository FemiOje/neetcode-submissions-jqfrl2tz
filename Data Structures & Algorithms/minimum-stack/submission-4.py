class MinStack:

    def __init__(self):
        self.stack = []
        self.lastMinimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.lastMinimum[-1] if self.lastMinimum else val)
        self.lastMinimum.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.lastMinimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.lastMinimum[-1]

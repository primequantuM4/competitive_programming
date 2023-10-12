class MinStack:

    def __init__(self):
        self.min_track = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_track or self.min_track[-1] >= val:
            self.min_track.append(val) 

    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.min_track[-1]:
            self.min_track.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
       return self.min_track[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

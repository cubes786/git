class MinStack:
    def __init__(self):
        self.data=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.data:
            last=self.data.pop()
            if self.min_stack and self.min_stack[-1]==last:
                self.min_stack.pop()

    def top(self)->int:
        return self.data[-1] if self.data else 0

    def getMin(self)->int:
        return self.min_stack[-1] if self.min_stack else 0
             

class MinStack:

    def __init__(self):
        self.stack = []
        self.extra_stack = []       

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.extra_stack:
            top_ele = self.extra_stack[len(self.extra_stack) - 1]
            self.extra_stack.append(min(val, top_ele))
        else:
            self.extra_stack.append(val)

    def pop(self) -> None:
        self.stack.pop(len(self.stack) - 1)
        self.extra_stack.pop(len(self.extra_stack) - 1)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.extra_stack[len(self.extra_stack) - 1]

        

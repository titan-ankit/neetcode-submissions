class MinStack:

    def __init__(self):
        self.stack = []
        #min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #min_stack.insert()

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top = self.stack[len(self.stack)-1]
        return top

    def getMin(self) -> int:
        min = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < min:
                min = self.stack[i]
        return min
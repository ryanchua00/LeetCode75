class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        currMin = self.minStack[-1] if len(self.minStack) > 0 else None
        self.stack.append(val)
        self.minStack.append(min(currMin, val) if currMin else val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    # call getMin repeatedly to get smallest element
    def getMin(self) -> int:
        return self.minStack[-1]

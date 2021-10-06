

class Stack:
    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = []
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
    def length(self):
        return len(self.stack)
    def top(self) -> int:
        return self.stack[-1]  
    def push(self, x):
        self.x = x
        self.stack.append(x)       
    def pop(self):
        self.stack.pop()

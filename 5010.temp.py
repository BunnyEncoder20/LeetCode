class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())

        # Insert new element
        self.st1.append(x)

        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        # Edge case
        if not self.st1:
            print("Stack is empty")
            return -1 

        # pop top element
        return self.st1.pop()

    def peek(self):
        # Edge case
        if not self.st1:
            print("Stack is empty")
            return -1

        # Return the top element
        return self.st1[-1]

    def is_empty(self):
        return not self.st1
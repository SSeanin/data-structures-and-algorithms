class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.insert(0, data)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

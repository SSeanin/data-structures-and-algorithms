# Stack implementation
class Stack:
    def __init__(self):
        self.data = []

    def push(self, *args):
        self.data.extend(args)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        for el in self.data:
            yield el


class DoubleEndedStack:
    def __init__(self):
        self.data = []
        self.front_size = 0
        self.back_size = 0

    def push_front(self, data):
        self.data.append(data)
        self.front_size += 1

    def push_back(self, data):
        self.data.insert(0, data)
        self.back_size += 1

    def pop_front(self):
        if self.front_size > 0:
            self.data.pop()
            self.front_size -= 1
        else:
            raise IndexError('Front Stack is Empty')

    def pop_back(self):
        if self.back_size > 0:
            self.data.pop(0)
            self.back_size -= 1
        else:
            raise IndexError('Back Stack is Empty')

    def __str__(self):
        return str(self.data)

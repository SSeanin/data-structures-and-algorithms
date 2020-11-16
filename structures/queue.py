from structures.stack import Stack


class Queue:
    def __init__(self):
        self.data = []

    def add(self, *args):
        self.data.extend(args)

    def delete(self):
        self.data.pop(0)

    def first(self):
        return self.data[0]

    def last(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def __iter__(self):
        for element in self.data:
            yield element


class CircularQueue:
    def __init__(self, size: int):
        self.data = [None] * 5
        self.size = size
        self.top = 0
        self.bottom = 0

    def add(self, data):
        if self.top + 1 == self.bottom and self.data[self.top + 2] is not None:
            raise IndexError('Queue is full')

        if self.top + 1 == self.size:
            if self.data[0] is None:
                self.data[0] = data
                self.top = 0
            else:
                raise IndexError('Queue is full')

        else:
            self.data[self.top] = data
            self.top += 1

    def delete(self):
        if self.bottom == self.top and self.data[self.bottom] is None:
            raise IndexError('Queue is empty')

        if self.bottom + 1 == self.size:
            element = self.data[self.bottom]
            self.bottom = 0
            self.data[-1] = None
            return element

        else:
            element = self.data[self.bottom]
            self.bottom += 1
            return element

    def bottom(self):
        return self.data[self.bottom]

    def top(self):
        return self.data[self.top]


class DoubleStackQueue:
    def __init__(self):
        self.main = Stack()
        self.tmp = Stack()

    def add(self, data):
        if self.main.is_empty():
            self.main.push(data)
        else:
            for element in self.main:
                self.tmp.push(element)

            self.main.push(data)

            for element in self.tmp:
                self.main.push(element)

    def delete(self):
        self.main.pop()

    def bottom(self):
        return self.main.peek()

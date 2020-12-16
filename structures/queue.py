from structures.stack import Stack
import structures.linkedlist as linked_list


class Queue:
    def __init__(self):
        self.data = []

    def add(self, *args):
        self.data.extend(args)

    def delete(self):
        return self.data.pop(0)

    def first(self):
        return self.data[0]

    def last(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        for element in self.data:
            yield element


class CircularQueue:
    def __init__(self, size: int):
        self.data = [None] * size
        self.tail = -1
        self.head = -1
        self.size = size

    def is_empty(self):
        return self.head == -1 and self.tail == -1

    def add(self, data):
        if self.tail == -1 and self.head == -1:
            self.head = 0
            self.tail = 0
            self.data[self.tail] = data
            return None

        elif (self.tail + 1) % self.size == self.head:
            raise IndexError('Queue is full')

        else:
            self.tail = (self.tail + 1) % self.size
            self.data[self.tail] = data

    def delete(self):
        if self.head == -1 and self.tail == -1:
            raise IndexError('Queue is empty')

        elif self.head == self.tail:
            element = self.data[self.head]
            self.head = -1
            self.tail = -1
            return element

        else:
            element = self.data[self.head]
            self.head = (self.head + 1) % self.size
            return element

    def __str__(self):
        return str(self.data)


class DoubleStackQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def add(self, data):
        self.push_stack.push(data)

    def delete(self):
        if len(self.pop_stack.data) == 0:
            if len(self.push_stack.data) == 0:
                raise IndexError('Queue is empty')
            for i in range(len(self.push_stack.data)):
                self.pop_stack.push(self.push_stack.pop())

        return self.pop_stack.pop()

    def bottom(self):
        if len(self.pop_stack.data) == 0:
            for i in range(self.push_stack.data):
                self.pop_stack.push(self.push_stack.pop())

        return self.pop_stack.peek()


class LinkedListQueue:
    def __init__(self):
        self.data = linked_list.LinkedList()

    def add(self, data):
        self.data.insert_first(data)

    def delete(self):
        return self.data.remove_tail()

    def __str__(self):
        return str([x for x in self.data])

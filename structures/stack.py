import structures.linkedlist as linked_list


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
        for element in self.data:
            yield element


# Double Ended Stack
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


class LinkedListStack:
    def __init__(self):
        self.data = linked_list.LinkedList()

    def push(self, data):
        self.data.insert_first(data)

    def pop(self):
        return self.data.remove_head()

    def __str__(self):
        return str([x for x in self.data])

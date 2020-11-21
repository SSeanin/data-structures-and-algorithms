class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next = next_element


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        self.head = Node(data, next_element=self.head.next)

    def insert_last(self, data):
        counter: Node = self.head

        while counter.next is not None:
            counter = counter.next

        counter.next = Node(data)

    def insert(self, index: int, data):
        counter = self.head

        try:
            for i in range(index):
                counter = counter.next
        except AttributeError:
            raise IndexError('Index out of bound')

        counter.next = Node(data, next_element=counter.next)

    def remove_first(self):
        first_element = self.head
        self.head = self.head.next
        return first_element

    def remove_last(self):
        if self.head is None or self.head.next is None:
            element = self.head
            self.head = None
            return element

        previous = self.head
        current = self.head.next

        while current.next is not None:
            previous = current
            current = current.next

        element = current
        previous.next = None

        return element

    def remove(self, index: int):
        if self.head is None or self.head.next is None:
            if index == 0:
                element = self.head
                self.head = None
                return element

            raise IndexError('Index out of bound')

        previous = self.head
        current = self.head.next

        try:
            for i in range(index + 1):
                previous = current
                current = current.next
        except AttributeError:
            raise IndexError('Index out of bound')

        previous.next = current.next

        return current

    def size(self) -> int:
        if self.head is None:
            return 0

        current = self.head
        counter = 1

        while current.next is not None:
            current = current.next
            counter += 1

        return counter

    def reverse(self):
        pass

    def get(self, index: int) -> Node:
        if self.head is None:
            raise IndexError('Index out of bound')

        current = self.head

        try:
            for i in range(index + 1):
                current = current.next
        except AttributeError:
            raise IndexError('Index out of bound')

        return current

    def tail(self) -> Node:
        if self.head is None:
            raise IndexError('Index out of bound')

        current = self.head

        while current.next is not None:
            current = current.next

        return current

    def mid(self) -> Node:
        if self.head is None:
            raise IndexError('Index out of bound')

        if self.head.next is None:
            return self.head

        fast = self.head
        slow = self.head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

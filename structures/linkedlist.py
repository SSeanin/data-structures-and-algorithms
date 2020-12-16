class Node:
    def __init__(self, data, next_element=None, previous_element=None):
        self.data = data
        self.next = next_element
        self.previous = previous_element

    def __str__(self):
        return f'{self.previous.data if self.previous is not None else None} ' \
               f'{self.data} ' \
               f'{self.next.data if self.next is not None else None}'


def insert_before_node(node: Node, new_node: Node):
    new_node.next = node
    new_node.previous = node.previous
    if node.previous is not None:
        node.previous.next = new_node
    node.previous = new_node


def delete_previous_node(node: Node):
    if node.previous is None:
        raise IndexError('No previous node found')

    node.previous.previous.next = node
    node.previous = node.previous.previous


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        self.head = Node(data, next_element=self.head if self.head is not None else None)

    def insert_last(self, data):
        counter: Node = self.head

        while counter.next is not None:
            counter = counter.next

        counter.next = Node(data)

    def insert(self, index: int, data):
        counter = self.head

        for i in range(index - 1):
            counter = counter.next

        counter.next = Node(data, next_element=counter.next)

    def remove_head(self):
        if self.head is None:
            raise IndexError('List is empty')

        first_element = self.head
        self.head = self.head.next
        return first_element.data

    def remove_tail(self):
        if self.head is None:
            raise IndexError('List is empty')

        if self.head.next is None:
            element = self.head
            self.head = None
            return element.data

        previous = self.head
        current = self.head.next

        while current.next is not None:
            previous = current
            current = current.next

        element = current
        previous.next = None

        return element.data

    def size(self) -> int:
        if self.head is None:
            return 0

        current = self.head
        counter = 1

        while current.next is not None:
            current = current.next
            counter += 1

        return counter

    def tail(self) -> Node:
        if self.head is None:
            raise IndexError('List is empty')

        current = self.head

        while current.next is not None:
            current = current.next

        return current.data

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

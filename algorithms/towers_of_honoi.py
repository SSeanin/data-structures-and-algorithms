from math import inf


class Disk:
    def __init__(self, weight: float):
        self.weight = weight

    def __str__(self):
        return self.weight


class Stack:
    def __init__(self, name: str):
        self.data = []
        self.name = name

    def push(self, data: Disk):
        self.data.append(data)

    def pop(self) -> Disk:
        return self.data.pop()

    def peek(self):
        try:
            return self.data[-1]
        except IndexError:
            return Disk(inf)

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


def legal_move(pole_a: Stack, pole_b: Stack):
    if pole_a.is_empty() and not pole_b.is_empty():
        print(f'Moving {pole_b.peek().weight} from {pole_b.name} to {pole_a.name}')
        pole_a.push(pole_b.pop())

    elif pole_b.is_empty() and not pole_a.is_empty():
        print(f'Moving {pole_a.peek().weight} from {pole_a.name} to {pole_b.name}')
        pole_b.push(pole_a.pop())

    elif pole_b.peek().weight > pole_a.peek().weight:
        print(f'Moving {pole_b.peek().weight} from {pole_b.name} to {pole_a.name}')
        pole_a.push(pole_b.pop())

    elif pole_a.peek().weight > pole_b.peek().weight:
        print(f'Moving {pole_a.peek().weight} from {pole_a.name} to {pole_b.name}')
        pole_b.push(pole_a.pop())


def towers(no_of_disks, src=Stack('A'), dest=Stack('C'), aux=Stack('B')):
    for i in range(1, no_of_disks + 1):
        src.push(Disk(i))

    if no_of_disks % 2 == 0:
        while dest.size() < no_of_disks:
            legal_move(src, aux)
            legal_move(src, dest)
            legal_move(aux, dest)

    else:
        while dest.size() < no_of_disks:
            legal_move(src, dest)
            legal_move(src, aux)
            if dest.size() < no_of_disks:
                legal_move(aux, dest)


if __name__ == '__main__':
    towers(3)

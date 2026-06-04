class Node:
    value: int
    prev: Node | None
    next: Node | None

    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        prev_value = self.prev.value if self.prev else None
        next_value = self.next.value if self.next else None
        return f"Node(value={self.value}, prev={prev_value}, next={next_value})"


class Deque:
    head: Node | None
    tail: Node | None

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return not self.head

    def append(self, value: int) -> None:
        new = Node(value)

        if self.isEmpty():
            self.head = new
            self.tail = new
            return

        new.prev = self.tail
        self.tail.next = new
        self.tail = new

    def appendleft(self, value: int) -> None:
        new = Node(value)

        if self.isEmpty():
            self.head = new
            self.tail = new
            return

        new.next = self.head
        self.head.prev = new
        self.head = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        result = self.tail.value

        if self.head is self.tail:
            self.head, self.tail = None, None
            return result

        prev = self.tail.prev
        prev.next = None
        self.tail = prev
        return result

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        result = self.head.value

        if self.head is self.tail:
            self.head, self.tail = None, None
            return result

        next = self.head.next
        next.prev = None
        self.head = next
        return result

    def __repr__(self):
        return f"Deque('head={self.head}', tail={self.tail})"

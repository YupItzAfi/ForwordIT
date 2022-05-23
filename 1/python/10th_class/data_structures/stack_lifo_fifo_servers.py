class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        self.next = None

    def __str__(self):
        cur = self.head.next
        out = ""

        while cur:
            out += str(cur.value)+", "
            cur = cur.next
        return out[:]

    def isEmpty(self):
        return self.value == 0

    def peek(self):
        if self.isEmpty():
            return "Peeking value is empty"
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self, value):
        if self.isEmpty():
            return "No values for pop"
        rem = self.head.next.next
        self.size -= 1
        return rem.value


stack = Stack()
stack.push(3)
stack.push(3)
stack.push(3)
stack.push(3)
stack.push(3)
stack.push(3)


print(stack)

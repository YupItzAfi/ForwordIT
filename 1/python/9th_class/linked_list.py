class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfterNode(self, prev_data, data):
        if prev_data is None:
            print("no previous data is there.")
            return None
        new_node = Node(data)
        new_node.next = prev_data.next
        prev_data.next = new_node


lst = Linked_List()
lst.head = Node(10)
sec = Node(20)
third = Node(30)

lst.head.next = sec
sec.next = third
lst.insertAfterNode(sec, 200)

lst.push(87967)

lst.print()

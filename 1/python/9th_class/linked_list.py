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


lst = Linked_List()
lst.head = Node(10)
sec = Node(20)
third = Node(30)

lst.head.next = sec
sec.next = third

lst.print()

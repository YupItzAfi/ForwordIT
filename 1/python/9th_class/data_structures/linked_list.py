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
            print(temp.data, end=" ")
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

    def deleteNode(self, data):
        temp = self.head

        if temp is not None:
            if temp.data == data:
                self.head = temp.head
                temp = None
                return
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None


lst = Linked_List()
# lst.head = Node(10)
# sec = Node(20)
# third = Node(30)

# lst.head.next = sec
# sec.next = third
lst.push(10)
lst.push(20)
lst.push(30)
lst.push(40)
lst.push(50)
lst.push(60)
lst.push(70)
lst.push(80)
lst.push(10)


lst.print()
lst.deleteNode(80)

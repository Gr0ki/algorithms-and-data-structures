from random import randint


class Node:
    def __init__(self, data=None, prev=None, next_node=None):
        self.data = data
        self.prev = prev
        self.next_node = next_node

    def __str__(self):
        return f"[{self.data}]->{self.next_node}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def random_data(self, length=1):
        if not self.head:
            self.head = Node(randint(0, 200))

        temp = self.head
        for i in range(length - 1):
            temp.next_node = Node(randint(0, 200), temp)
            temp = temp.next_node

    def append(self, element):
        if not self.head:
            self.head = Node(element)
            return
        else:
            temp = self.head

        while temp.next_node:
            temp = temp.next_node
        else:
            temp.next_node = Node(element)
            temp.next_node.prev = temp

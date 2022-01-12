from random import randint


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'[{self.data}] -> {self.next_node}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    @staticmethod
    def __go_to_last_elem(temp, do_count: bool=False, __count: int=0):
        while temp.next_node:
            if do_count:
                __count += 1
            temp = temp.next_node
        if do_count:
            return temp, __count
        else:
            return temp

    @staticmethod
    def __go_to_elem(temp, index: int):                                     # ERROR
        if temp is not None:
            _, length = temp.__go_to_last_elem(temp, do_count=True)
        else:
            print('Error: Linked List is empty!')
            exit()

        if 0 <= index <= length - 1:
            for i in range(index + 1):
                temp = temp.next_node
            return temp
        else:
            print('Error: index out of range!')

    def random_data(self, length=1):
        if not self.head and length > 1:
            self.head = Node(randint(0, 1000))
            temp = self.head
            for i in range(length - 1):
                temp = self.__go_to_last_elem(temp)
                temp.next_node = Node(randint(0, 1000))

        elif not self.head and length == 1:
            self.head = Node(randint(0, 1000))

        elif self.head and length >= 1:
            temp = self.head
            for i in range(length):
                temp = self.__go_to_last_elem(temp)
                temp.next_node = Node(randint(0, 1000))

        else:
            print('\nError: For random_data method length can\'t be less than 1!\n')

    def append(self, element):
        if not self.head:
            self.head = Node(element)
            return

        temp = self.__go_to_last_elem(self.head)
        temp.next_node = Node(element)
        return

    def pop(self, index=None):                                      # ERROR
        temp, length = self.__go_to_last_elem(self.head, do_count=True)
        if index is None:
            print(f'self.head')                                     # ERROR
            temp.head = None
        else:
            temp = self.__go_to_elem(temp, int(input('Enter ')))
            print(f'temp.head')                                     # ERROR
            temp.head = None

    def insert(self, index, data):
        pass

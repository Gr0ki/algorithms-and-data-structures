from classes import DoublyLinkedList
from functions import input_list_length, input_data


d_linked_list = DoublyLinkedList()
d_linked_list.random_data(input_list_length())
d_linked_list.append(input_data())
print(d_linked_list)

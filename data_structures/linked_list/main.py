from classes import LinkedList
from functions import input_int


linked_list = LinkedList()
linked_list.append(input_int('append'))
print(linked_list)
linked_list.append(input_int('append'))
print(linked_list)
linked_list.random_data(4)
print(linked_list)

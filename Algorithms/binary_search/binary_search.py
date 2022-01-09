import parser
from random import randint
from math import ceil
import time


def welcome():
    print('''\nWelcome to the game "Guess the name"!
Rules is simple: choose a name from a list and algorithm to use.
The goal is to tests search algorithms efficiency.
Remember, you can quit anytime you want, just enter "Exit" in any input field.\n''')


def get_names_list() -> list:
    print('Hold on, parsing names for you...')
    requested_names_number = 214
    names_parser = parser.NamesParser(requested_names_number)
    return names_parser.parse()


def print_names(names_list: list):
    print('\nHere is the names for this game:\n''')
    for i in range(ceil(len(names_list) / 10)):
        print(f'{", ".join(names_list[:10])}')
        names_list = names_list[10:]


def choose_name() -> str:
    return input('\nPlease, choose a name to search using one of the algorithms: ')


def chosen_name_validator(selected_name) -> str:
    """
    Check if input data is valid and resend request if needed.
    """
    match selected_name:
        case selected_name if selected_name in names:
            return selected_name
        case 'exit' | 'Exit':
            print('\nSee you later.')
            exit()
        case _:
            print('Woops... This name isn\'t in a list. Please try again.')
            chosen_name_validator(choose_name())


def list_method_index(names_list: list, selected_name: str):
    start_time = time.time()
    _ = names_list.index(selected_name)
    print(f'It takes {(time.time() - start_time):.7f}')


def consistent_search(names_list: list, selected_name: str):
    start_time = time.time()
    attempt_number = 0
    for index in range(len(names_list)):
        attempt_number += 1
        if selected_name == names_list[index]:
            print(f'It takes {(time.time() - start_time):.7f} and {attempt_number=}')
            break


def random_search(names_list: list, selected_name: str):
    start_time = time.time()
    attempt_number = 0
    while True:
        attempt_number += 1
        index = randint(0, len(names_list) - 1)
        if selected_name == names_list[index]:
            print(f'It takes {(time.time() - start_time):.7f} and {attempt_number=}')
            break


def binary_search(names_list: list, selected_name: str):
    start_time = time.time()
    attempt_number, low, high = 0, 0, len(names_list) - 1
    while low <= high:
        attempt_number += 1
        mid = (low + high) // 2
        guess = names_list[mid]
        if guess == selected_name:
            print(f'It takes {(time.time() - start_time):.7f} and {attempt_number=}')
            break
        elif guess > selected_name:
            high = mid - 1
        else:
            low = mid + 1


def choose_algorithm(names_list: list, selected_name: str):
    """
    Take user's choice and run a selected algorithm or remake request from a user.
    """
    algorithm_number = input(
        'Enter a number of search algorithm '
        '(1 - list.index(), 2 - consistent search, 3 - random search, 4 - binary search): '
    )
    match algorithm_number:
        case '1':
            list_method_index(names_list, selected_name)
        case '2':
            consistent_search(names_list, selected_name)
        case '3':
            random_search(names_list, selected_name)
        case '4':
            binary_search(names_list, selected_name)
        case 'exit':
            print('\nSee you later.')
            exit()
        case _:
            print('Woops... Wrong number. Please try again.')
            choose_algorithm(names_list, selected_name)


def continue_or_exit_handler(names_list: list, selected_name: str):
    """
    Ask user if he wants to quit or choose another algorithm.
    """
    answer = input('Do you wanna choose another algorithm for this name? (yes/no): ')
    match answer:
        case 'Y' | 'y' | 'Yes' | 'yes':
            choose_algorithm(names_list, selected_name)
        case 'N' | 'n' | 'No' | 'no' | 'exit' | 'Exit':
            print('OK. Logging out.')
            exit()
        case _:
            print('Woops... can\' process this. Logging out.')
            exit()


welcome()
names = get_names_list()
print_names(names)
chosen_name = choose_name()
chosen_name_validator(chosen_name)
choose_algorithm(names, chosen_name)
while True:
    continue_or_exit_handler(names, chosen_name)

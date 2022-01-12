def input_list_length():
    try:
        int_value = int(input("Enter list length (positive integer value): "))
        if int_value < 0:
            raise BaseException
        else:
            return int_value
    except BaseException:
        print("Something went wrong. Try again please.")
        input_list_length()


def input_data():
    try:
        int_value = int(input("Enter integer value: "))
        return int_value
    except BaseException:
        print("Something went wrong. Try again please.")
        input_data()
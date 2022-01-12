def input_int(method: str) -> int:
    try:
        match method:
            case 'append':
                method = 'to append the list'
            case 'pop':
                method = 'as index or skip this request to remove last item in the list'
        int_value = int(input(f'Enter integer value {method}: '))
        return int_value
    except BaseException:
        print("Something went wrong. Try again please.")
        input_int()
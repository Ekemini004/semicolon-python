
numbers = [number for number in range(1, 11)]


def square_number(any_list):

    return any_list * any_list


print(list(map(square_number, numbers)))

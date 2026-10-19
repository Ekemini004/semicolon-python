

list_one = [(1, 'A'), (4, 'B'),(2, 'C')]

def is_greater_thanTwo(any_list):

    return any_list[0] > 2

new_list = filter(is_greater_thanTwo, list_one)

print(list(new_list))



list_one = [ num for num in range(1,21)]

print(list_one)

def is_even (any_list):

    return any_list % 2 == 0


even_list = filter(is_even, list_one)

print(list(even_list))

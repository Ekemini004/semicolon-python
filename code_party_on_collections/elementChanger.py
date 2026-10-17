
numbers = (1, 2, [3,4], 5)

numbers_list = list(numbers)

numbers_list.pop(2)

numbers_list.insert(2, 99)

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)

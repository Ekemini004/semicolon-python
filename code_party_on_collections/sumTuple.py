
from functools import reduce

list_of_tuples =  [(1, 2), (3, 4), (5,6)]

def add(item_a, item_b):

    return item_a + item_b


new_list = [reduce(add, tuple_item) for tuple_item in list_of_tuples]

print(new_list)


def is_greater_than_five(any_list):

    return any_list > 5


result = list(filter(is_greater_than_five, new_list))

print(result)

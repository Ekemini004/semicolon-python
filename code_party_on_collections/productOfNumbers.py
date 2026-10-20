from functools import reduce 

def square_items(any_list_item):

    return any_list_item * any_list_item



numbers = [1,2,3,4]

list(map(square_items, numbers))


def product_numbers(item_a, item_b):

    return item_a * item_b


result = reduce(product_numbers, numbers)

print(result)

from functools import reduce 

items =  ['123', '456', '789','abc', 'def']

new_item = [ int(item) for item in items if(str.isdigit(item) == True) ]


print(new_item)


def add_numbers(list_item_a, list_item_b):

    return list_item_a + list_item_b



result = reduce(add_numbers, new_item)

print(result)

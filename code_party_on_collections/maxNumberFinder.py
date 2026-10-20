from functools import reduce 

numbers = [3, 5, 9, 2, 8]

def find_max(list_item_a, list_item_b):

    if(list_item_a > list_item_b):

        return list_item_a

    else:
        
        return list_item_b



maximum = reduce(find_max, numbers)

print(maximum)

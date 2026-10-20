prices  = [100, 200, 300]

def add_tax(any_list):

    return any_list + (0.1*any_list)


print(list(map(add_tax, prices)))

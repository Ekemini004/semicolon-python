names = ['john', 'mary','steve']

def to_uppercase(any_list):

    return any_list[0].upper()


print(list(map(to_uppercase, names)))
